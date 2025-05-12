# POD System

## Description
This is a Proof of Delivery (POD) system built with FastAPI. It allows you to assign deliveries, confirm deliveries using OTP, generate Proof of Delivery (POD) receipts, and download them.

## Features
- **Assign Delivery**: Assign deliveries and generate OTP.
- **Confirm Delivery**: Confirm delivery using OTP and location.
- **Generate POD**: Generate Proof of Delivery (POD) receipt.
- **Download POD**: Download the POD receipt as a PDF.
- **Get Deliveries**: View all assigned deliveries.

## API Endpoints

### 1. Assign Delivery
- **Endpoint**: `POST /assign_delivery`
- **Request Body**:
  ```json
  {
    "id": "string",
    "customer_name": "string",
    "location": "string"
  }
 - **Response**:
    ```json
      {
        "message": "Delivery assigned successfully",
        "otp": 123456
      }
### 2. Confirm Delivery
- **Endpoint**: `POST /confirm_delivery/{delivery_id}`
- **Request Body**:
  ```json
  {
  "otp": 123456,
  "location": "string"
}

 - **Response**:
    ```json
      {
        "message": "Delivery confirmed",
        "POD": {
          "Delivery ID": "string",
          "Customer Name": "string",
          "Location": "string",
          "Timestamp": "string",
          "OTP Used": 123456,
          "PDF Path": "string"
              }
      } 
### 3. Generate POD
- **Endpoint**: `POST /generate_pod/{delivery_id}`
- **Response**:
    ```json
     {
      "POD Receipt": {
      "Delivery ID": "string",
      "Customer Name": "string",
      "Delivery Location": "string",
      "Timestamp": "string",
      "OTP Used": 123456
    }
}

### 4. Get All Deliveries
- **Endpoint**: `GET /get_deliveries`
- **Response**:
    ```json
     {
  "DEL123": {
    "id": "DEL123",
    "customer_name": "John Doe",
    "location": "New York",
    "otp": 123456,
    "delivered": false,
    "timestamp": null
  }
}

### 5. Download POD PDF
- **Endpoint**: `GET /download_pod/{delivery_id}`
- **Response**: Returns a downloadable PDF of the POD.

### Live URL
  Access the live API at the following URL:
   https://your-app-name.up.railway.app
### Running Locally
**Clone the repository**.
**Install dependencies:**
    pip install -r requirements.txt
**Run the application:**
    uvicorn pod_system:app --reload
Access the API at http://127.0.0.1:8000.
### Deployment
This project is deployed on Railway. You can access it live at the URL mentioned above. For further details, refer to the deployment section in the Railway dashboard.

