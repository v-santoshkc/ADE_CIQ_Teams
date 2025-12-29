from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, Any

from data import DATA_STORE, get_data

app = FastAPI(title="Customer IQ Backend", version="1.0.0")

# ======================
# CORS (Teams + ngrok)
# ======================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ======================
# MODELS
# ======================
class UpdateRequest(BaseModel):
    csamId: str
    customerName: str
    updatedData: Dict[str, Any]

# ======================
# ENDPOINTS
# ======================
@app.get("/get_data")
def read_data():
    return get_data()

@app.post("/update_customer")
def update_customer(payload: UpdateRequest):
    for csam_wrapper in DATA_STORE:
        csam = csam_wrapper["csam"]
        if csam["csamId"] == payload.csamId:
            for i, cust in enumerate(csam["customers"]):
                if cust["customerName"] == payload.customerName:
                    csam["customers"][i] = payload.updatedData
                    return {
                        "status": "success",
                        "updatedCustomer": payload.updatedData
                    }
    return {"status": "error", "message": "Customer not found"}

@app.get("/health")
def health():
    return {"status": "ok"}
