from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random, datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os 
from fastapi.responses import FileResponse


app = FastAPI()

class Delivery(BaseModel):
    id: str
    customer_name: str
    location: str
    otp: int = None
    delivered: bool = False
    timestamp: str = None

class ConfirmInput(BaseModel):
    otp: int
    location: str

deliveries = {}

@app.post("/assign_delivery")
def assign(delivery: Delivery):
    delivery.otp = random.randint(100000, 999999)
    deliveries[delivery.id] = delivery
    return {"message": "Delivery assigned successfully", "otp": delivery.otp}

@app.post("/confirm_delivery/{delivery_id}")
def confirm(delivery_id: str, confirmation: ConfirmInput):
    d = deliveries.get(delivery_id)
    if not d or d.otp != confirmation.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP")

    d.delivered = True
    d.timestamp = str(datetime.datetime.now())
    d.location = confirmation.location
    def create_pod_pdf(delivery):
        
        filename = f"{delivery.id}_POD.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        
        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, 750, "Proof of Delivery (POD) Receipt")

        c.setFont("Helvetica", 12)
        c.drawString(100, 720, f"Delivery ID: {delivery.id}")
        c.drawString(100, 700, f"Customer Name: {delivery.customer_name}")
        c.drawString(100, 680, f"Delivery Location: {delivery.location}")
        c.drawString(100, 660, f"Timestamp: {delivery.timestamp}")
        c.drawString(100, 640, f"OTP Used: {delivery.otp}")
        
        c.save()
        return filename

     

    # 🔥 Generate POD PDF instantly
    pdf_path = create_pod_pdf(d)

    return {
        "message": "Delivery confirmed",
        "POD": {
            "Delivery ID": d.id,
            "Customer Name": d.customer_name,
            "Location": d.location,
            "Timestamp": d.timestamp,
            "OTP Used": d.otp,
            "PDF Path": pdf_path
        }
    }


@app.post("/generate_pod/{delivery_id}")
def generate_pod(delivery_id: str):
    d = deliveries.get(delivery_id)
    if not d or not d.delivered:
        raise HTTPException(status_code=404, detail="Delivery not found or not yet confirmed")
    pod = {
        "Delivery ID": d.id,
        "Customer Name": d.customer_name,
        "Delivery Location": d.location,
        "Timestamp": d.timestamp,
        "OTP Used": d.otp
    }
    return {"POD Receipt": pod}

@app.get("/get_deliveries")
def get_all():
    return deliveries
@app.get("/download_pod/{delivery_id}")
def download_pod(delivery_id: str):
    """Download the generated POD PDF"""
    filename = f"{delivery_id}_POD.pdf"
    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="POD PDF not found")
    return FileResponse(path=filename, filename=filename, media_type='application/pdf')