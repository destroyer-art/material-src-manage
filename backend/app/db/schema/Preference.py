from app import dbHandler
from sqlalchemy import Column, String
from app.db.dbconnect import Base


class PreferenceSchema(Base):
    __tablename__ = "Preference"

    ID = Column(String, primary_key=True)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    grade = Column(String, nullable=True)
    choice = Column(String, nullable=True)
    min_width = Column(String, nullable=True)
    max_width = Column(String, nullable=True)
    min_thickness = Column(String, nullable=True)
    max_thickness = Column(String, nullable=True)