from fastapi import APIRouter

health_api = APIRouter()


@health_api.get("/health")
def health_check():
    return {"Status": "OK", "Message": "Server is running!"}
