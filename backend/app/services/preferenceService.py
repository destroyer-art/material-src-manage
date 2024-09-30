from app.db.dbconnect import SessionLocal
from app.db.schemas import PreferenceSchema

dbHandler = SessionLocal()


async def get_preference_data(id: None | int):
    if id is None:
        return dbHandler.query(PreferenceSchema).all()
    else:
        return dbHandler.query(PreferenceSchema).filter(PreferenceSchema.id == id).first()