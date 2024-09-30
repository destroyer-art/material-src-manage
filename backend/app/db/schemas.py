from sqlalchemy import Column, String, Integer
from app.db.dbconnect import Base


class InventorySchema(Base):
    __tablename__ = "Inventory"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    product_number = Column(String, nullable=False)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    choice = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    finish = Column(String, nullable=False)
    surface = Column(String, nullable=True)
    quantity = Column(String, nullable=True)
    weight = Column(String, nullable=False)
    length = Column(String, nullable=True)
    width = Column(String, nullable=True)
    height = Column(String, nullable=True)
    thickness = Column(String, nullable=True)
    outer_diameter = Column(String, nullable=True)
    wall_thickness = Column(String, nullable=True)
    web_thickness = Column(String, nullable=True)
    flange_thickness = Column(String, nullable=True)
    certificates = Column(String, nullable=True)
    location = Column(String, nullable=False)


class PreferenceSchema(Base):
    __tablename__ = "Preference"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    grade = Column(String, nullable=True)
    choice = Column(String, nullable=True)
    min_width = Column(String, nullable=True)
    max_width = Column(String, nullable=True)
    min_thickness = Column(String, nullable=True)
    max_thickness = Column(String, nullable=True)
