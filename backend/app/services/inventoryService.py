from app.db.dbconnect import SessionLocal
from app.db.schemas import InventorySchema
from app.models.preference import PreferenceModel
from sqlalchemy import and_

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


async def get_match_inventory(preference: PreferenceModel):
    return (
        dbHandler.query(InventorySchema)
        .filter(
            and_(
                InventorySchema.material == preference.material,
                InventorySchema.form == preference.form,
                InventorySchema.grade == preference.grade,
                InventorySchema.choice == preference.choice,
                InventorySchema.width >= preference.min_width,
                InventorySchema.width <= preference.max_width,
                InventorySchema.thickness >= preference.min_thickness,
                InventorySchema.thickness <= preference.max_thickness,
            )
        )
        .order_by(InventorySchema.weight.desc())
    )
