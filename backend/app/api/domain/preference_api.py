from fastapi import APIRouter, Query
from app.services import preferenceService

preference_api = APIRouter()


@preference_api.get("/")
async def get_preference_info(id: int = Query(default=None, ge=1)):
    result = await preferenceService.get_preference_data(id)
    return result
