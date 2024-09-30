from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/health_check")
def health_check():
    return {"Message": "Server is Running"}
