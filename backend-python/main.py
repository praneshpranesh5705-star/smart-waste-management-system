from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel, Field
app=FastAPI(title="EcoGrid AI API",version="1.0")
class BinTelemetry(BaseModel):
    device_id:str
    fill_percent:float=Field(ge=0,le=100)
    temperature_c:float=Field(ge=-20,le=100)
    battery_percent:float=Field(ge=0,le=100)
bins=[{"device_id":"SW-204","fill_percent":94,"temperature_c":31,"battery_percent":87,"location":"Market Road"}]
def predict_overflow(fill_percent:float,fill_rate_per_hour:float=8.0):
    hours=0 if fill_percent>=100 else (100-fill_percent)/max(fill_rate_per_hour,.1)
    risk="CRITICAL" if hours<1 else "HIGH" if hours<3 else "MEDIUM" if hours<8 else "LOW"
    return {"hours_to_overflow":round(hours,2),"risk":risk}
@app.get("/api/health")
def health(): return {"status":"online","service":"EcoGrid Python AI","models":["overflow","anomaly"]}
@app.get("/api/bins")
def get_bins(): return {"count":len(bins),"bins":bins}
@app.post("/api/telemetry")
def telemetry(data:BinTelemetry,x_api_key:str|None=Header(default=None)):
    if x_api_key not in {"demo-key","smart-waste-key"}: raise HTTPException(status_code=401,detail="Invalid API key")
    result=data.model_dump();result["prediction"]=predict_overflow(data.fill_percent);bins.append(result)
    return {"accepted":True,**result}
