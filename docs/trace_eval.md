# 📊 BÁO CÁO THU HOẠCH NGHIỆM THU BÀI LAB 3 (BƯỚC 3 — SUBMISSION ARTIFACT)

> **Họ và Tên Học viên:** [Điền Họ và Tên]
> **Mã Sinh Viên / Mã Học viên:** [Điền MSSV]
> **Chủ đề Lựa chọn:** [Điền tên chủ đề đã chọn từ docs/DANH_SACH_DE_TAI.md hoặc Đề tài Mở]

---

## 1. BẢNG CHẤM ĐIỂM AGENTIC FIT SCORING MATRIX (ĐÁNH GIÁ CHỦ ĐỀ)

| Tiêu chí Đánh giá             | Mức độ (1 - 5) | Giải trình chi tiết lý do chọn điểm                                                                                                                                      |
| :--------------------------------- | :---------------: | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **1. Multi-step Reasoning**  |       5 / 5       | Bài toán yêu cầu tra cứu vị trí, tình trạng của sách, kiểm tra xem ai đang mượn trước khi đưa ra quyết định hoặc cho phép gia hạn.                     |
| **2. Tool Interaction**      |       5 / 5       | Hệ thống cần kết nối với MCP Server để truy vấn cơ sở dữ liệu thư viện (`library_query`) và thực hiện thao tác cập nhật hệ thống (`renew_document`). |
| **3. Dynamic Decision**      |       5 / 5       | Việc gia hạn sách phụ thuộc vào kết quả của bước tra cứu (chỉ cho phép gia hạn nếu đúng sinh viên đang mượn sách đó).                                  |
| **4. Long Horizon Goal**     |       4 / 5       | Phải ghi nhớ thông tin về tài liệu và người dùng qua các bước tra cứu và gia hạn.                                                                               |
| **TỔNG ĐIỂM AGENTIC FIT** | **19 / 20** | *Nếu tổng điểm > 12/20: Bài toán rất phù hợp triển khai Agentic System.*                                                                                            |

---

## 2. TRÍCH XUẤT KẾT QUẢ WATERFALL TRACE LOG (SAU KHI CHẠY TEST SUITE TRÊN API THẬT)

> ⚠️ **YÊU CẦU NGHIỆM THU:** Mở tệp `.env` điền `GEMINI_API_KEY` (hoặc `OPENAI_API_KEY`) để kết nối LLM thật trước khi thực thi `python src/app.py --all`. Bài nộp chỉ dùng Mock Offline Provider sẽ không đạt điểm nghiệm thực tế.

Dán 1 đoạn trích xuất log tiêu biểu từ file `docs/trace_waterfall.json` sinh ra từ phản hồi LLM API thật:

```json
  {
    "step": 1,
    "query": "Tôi là sinh viên SV2026001, tôi muốn gia hạn quyển sách có mã DOC2026001 đến ngày 25/09/2026.",
    "action_type": "TOOL_EXECUTION",
    "tool_name": "renew_document",
    "arguments": {
      "document_id": "DOC2026001",
      "student_id": "SV2026001",
      "new_due_date": "25/09/2026"
    },
    "observation": {
      "status": "SUCCESS",
      "renewal_id": "RN-DOC2026001-SV2026001",
      "document_id": "DOC2026001",
      "new_due_date": "25/09/2026",
      "student_id": "SV2026001",
      "message": "Gia hạn thành công tài liệu DOC2026001 cho sinh viên SV2026001 đến ngày 25/09/2026."
    },
    "latency_ms": 3827.55
  }
```

---

## 3. TỔNG KẾT KẾT QUẢ NGHIỆM THU & NỘP BÀI

- [X] Đã điền API Key thật trong `.env` và xác nhận Agent chạy mượt mà trên LLM API thật (Gemini).

- **Tổng số Test Cases đã chạy thành công:** 5 / 5 test cases.
- **Số lượt gọi Tool qua MCP Server chính xác:** 4 lượt.
- **Kết quả đẩy Repo nộp bài:** [ ] Đã Commit và Push mã nguồn thành công lên GitHub cá nhân.
