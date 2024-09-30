from fastapi import APIRouter, Response

health_api = APIRouter()

@health_api.get("/health")
def health_check():
    return {"Status": "OK", "Message": "Server is running!"}