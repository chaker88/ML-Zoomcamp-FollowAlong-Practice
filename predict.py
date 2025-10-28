import pickle
import json
from fastapi import FastAPI
import uvicorn
from typing import Dict, Any
from pydantic import BaseModel, Field
from typing import Literal

# Define the Customer data model using Pydantic
# This class validates the input data structure and types
class Customer(BaseModel):
    # Customer demographic features
    gender: Literal["male", "female"]
    seniorcitizen: Literal[0, 1]
    partner: Literal["yes", "no"]
    dependents: Literal["yes", "no"]
    
    # Phone service related features
    phoneservice: Literal["yes", "no"]
    multiplelines: Literal["no", "yes", "no_phone_service"]
    
    # Internet service related features
    internetservice: Literal["dsl", "fiber_optic", "no"]
    onlinesecurity: Literal["no", "yes", "no_internet_service"]
    onlinebackup: Literal["no", "yes", "no_internet_service"]
    deviceprotection: Literal["no", "yes", "no_internet_service"]
    techsupport: Literal["no", "yes", "no_internet_service"]
    streamingtv: Literal["no", "yes", "no_internet_service"]
    streamingmovies: Literal["no", "yes", "no_internet_service"]
    
    # Contract and billing features
    contract: Literal["month-to-month", "one_year", "two_year"]
    paperlessbilling: Literal["yes", "no"]
    paymentmethod: Literal[
        "electronic_check",
        "mailed_check",
        "bank_transfer_(automatic)",
        "credit_card_(automatic)",
    ]
    
    # Numerical features with validation
    tenure: int = Field(..., ge=0)  # Must be non-negative integer
    monthlycharges: float = Field(..., ge=0.0)  # Must be non-negative float
    totalcharges: float = Field(..., ge=0.0)  # Must be non-negative float

# Define the response model for predictions
class PredictResponse(BaseModel):
    churn_probability: float
    churn_decision: bool

# Initialize FastAPI application
app = FastAPI(title="churn-prediction")

# Load the pre-trained model pipeline from file
with open("model.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

# Helper function to make predictions for a single customer
def predict_single(customer):
    # Get probability of class 1 (churn)
    result = pipeline.predict_proba(customer)[0,1]
    return float(result)

# API endpoint for making predictions
@app.post("/predict")
def predict(customer:Customer) -> PredictResponse:
    # Get churn probability
    prob = predict_single(customer.dict())
    # Return probability and binary decision (churn if prob >= 0.5)
    return PredictResponse(
            churn_probability= prob,
            churn_decision= bool(prob >= 0.5)
        )

# Run the FastAPI application if script is executed directly
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)

