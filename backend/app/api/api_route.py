from fastapi import APIRouter
from app.api.domain.preference_api import preference_api as preference_route

api_router = APIRouter()


@api_router.get("/health_check")
def health_check():
    return {"Message": "Server is Running"}


api_router.include_router(preference_route, prefix="/preference")
