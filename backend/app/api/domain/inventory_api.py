from fastapi import APIRouter, Query

from app.services import inventoryService

inventory_api = APIRouter()


@inventory_api.get("/")
async def health_check(page: int = Query(1, ge=1), perpage: int = Query(10, ge=5)):
    result = await inventoryService.get_inventory_data(page=page, perpage=perpage)
    return result
