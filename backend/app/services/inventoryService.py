from app.db.dbconnect import SessionLocal
from app.db.schemas import InventorySchema

dbHandler = SessionLocal()


async def get_inventory_data(page: int, perpage: int):
    offset = (page - 1) * perpage
    return (
        dbHandler.query(InventorySchema)
        .order_by(InventorySchema.weight.desc())
        .offset(offset)
        .limit(perpage)
        .all()
    )
