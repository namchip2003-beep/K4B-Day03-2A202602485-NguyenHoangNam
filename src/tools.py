"""
🛠️ TOOL DEFINITIONS & EXECUTION BACKEND
Mã nguồn chứa danh sách Tool Schemas (JSON Schema) và Execution Layer phục vụ cho MCP Server.
"""

import json
from typing import Dict, Any

# ==============================================================================
# 1. KHAI BÁO TOOL SCHEMAS CHUẨN NATIVE JSON SCHEMA (TASK 1.2)
# ==============================================================================

TOOLS_SCHEMA = [
    # Tool 1: Tra cứu tài liệu
    {
        "name": "library_query",
        "description": "Tra cứu thông tin, vị trí và tình trạng mượn/trả của sách/tài liệu trong thư viện.",
        "parameters": {
            "type": "object",
            "properties": {
                "document_id": {
                    "type": "string",
                    "description": "Mã tài liệu cần tra cứu (ví dụ: 'DOC2026001')"
                }
            },
            "required": ["document_id"]
        }
    },
    
    # --------------------------------------------------------------------------
    # TODO 1.2: HỌC VIÊN HOÀN THIỆN TOOL SCHEMA CHO 'renew_document'
    # 🎯 YÊU CẦU THIẾT KẾ SCHEMA (JSON SCHEMA STANDARD):
    # 1. Tool dùng để gia hạn tài liệu thư viện.
    # 2. Thiết kế các tham số (properties) để LLM trích xuất:
    #    - document_id (string): Mã tài liệu cần gia hạn (ví dụ: 'DOC2026001')
    #    - new_due_date (string): Thời gian hạn trả mới mong muốn (ví dụ: '25/09/2026')
    #    - student_id (string): Mã sinh viên đang mượn
    # 3. Khai báo danh sách các trường bắt buộc (required).
    # --------------------------------------------------------------------------
    {
        "name": "renew_document",
        "description": "Gia hạn thời gian mượn sách/tài liệu thư viện.",
        "parameters": {
            "type": "object",
            "properties": {
                "document_id": {
                    "type": "string",
                    "description": "Mã tài liệu cần gia hạn (ví dụ: 'DOC2026001')"
                },
                "new_due_date": {
                    "type": "string",
                    "description": "Thời gian hạn trả mới mong muốn (ví dụ: '25/09/2026')"
                },
                "student_id": {
                    "type": "string",
                    "description": "Mã sinh viên đang mượn sách"
                }
            },
            "required": ["document_id", "new_due_date", "student_id"]
        }
    }
]

# ==============================================================================
# 2. MÔ PHỎNG DỮ LIỆU & HÀM THỰC THI TOOL (EXECUTION LAYER)
# ==============================================================================

MOCK_DATABASE = {
    "DOC2026001": {
        "title": "Artificial Intelligence: A Modern Approach",
        "author": "Stuart Russell, Peter Norvig",
        "location": "Tầng 3, Khu Kỹ thuật",
        "status": "Đang cho mượn",
        "borrower_id": "SV2026001",
        "due_date": "15/09/2026"
    },
    "DOC2026002": {
        "title": "Clean Code",
        "author": "Robert C. Martin",
        "location": "Tầng 2, Khu IT",
        "status": "Sẵn sàng",
        "borrower_id": None,
        "due_date": None
    }
}


def execute_library_query(document_id: str) -> str:
    """Thực thi tra cứu tài liệu theo mã tài liệu"""
    document = MOCK_DATABASE.get(document_id.strip().upper())
    if document:
        return json.dumps({
            "status": "SUCCESS",
            "document_id": document_id,
            "data": document
        }, ensure_ascii=False)
    else:
        return json.dumps({
            "status": "NOT_FOUND",
            "message": f"Không tìm thấy dữ liệu tài liệu có mã '{document_id}'"
        }, ensure_ascii=False)


def execute_renew_document(document_id: str, new_due_date: str, student_id: str) -> str:
    """Thực thi gia hạn tài liệu"""
    return json.dumps({
        "status": "SUCCESS",
        "renewal_id": f"RN-{document_id}-{student_id}",
        "document_id": document_id,
        "new_due_date": new_due_date,
        "student_id": student_id,
        "message": f"Gia hạn thành công tài liệu {document_id} cho sinh viên {student_id} đến ngày {new_due_date}."
    }, ensure_ascii=False)


# Router gọi tool thực tế
TOOL_ROUTER = {
    "library_query": execute_library_query,
    "renew_document": execute_renew_document
}

def dispatch_tool_call(tool_name: str, arguments: Dict[str, Any]) -> str:
    """Hàm trung chuyển thực thi tool"""
    if tool_name in TOOL_ROUTER:
        try:
            return TOOL_ROUTER[tool_name](**arguments)
        except Exception as e:
            return json.dumps({"status": "EXECUTION_ERROR", "error": str(e)}, ensure_ascii=False)
    return json.dumps({"status": "UNKNOWN_TOOL", "error": f"Tool '{tool_name}' không tồn tại!"}, ensure_ascii=False)
