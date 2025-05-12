# 📦 Proof of Delivery (POD) System – FastAPI

A lightweight FastAPI backend to manage delivery assignments, verify OTP-based confirmations, generate and download Proof of Delivery (POD) PDFs.

---

## 🚀 Features

- 📬 Assign deliveries with OTP generation
- 🔐 Confirm deliveries via OTP + location
- 🧾 Auto-generate POD PDF upon confirmation
- 📥 Download POD as a PDF
- 📦 View all assigned deliveries

---

## 🛠 Setup

### 1. Clone & Install

```bash
git clone https://github.com/your-username/pod-system.git
cd pod-system
pip install fastapi uvicorn reportlab

**2. Run the API**
uvicorn pod_system:app --reload

**API Endpoints**
**➕ Assign Delivery**

**POST /assign_delivery**
Body:

{
  "id": "DEL123",
  "customer_name": "Alice",
  "location": "New York"
}
**✅ Confirm Delivery**

**POST /confirm_delivery/{delivery_id}**
Body:

{
  "otp": 123456,
  "location": "New York"
}
**🧾 Generate POD Metadata**

**POST /generate_pod/{delivery_id}**
**📥 Download POD PDF**

**GET /download_pod/{delivery_id}**
**📋 Get All Deliveries**

GET /get_deliveries
📂 Output Example
A successful confirmation generates a PDF:
DEL123_POD.pdf
🧠 Tech Stack
FastAPI – Web API framework

ReportLab – PDF generation

Uvicorn – ASGI server

💡 Use Cases
E-commerce delivery confirmation

Field service logging

Digital proof receipts with download links


