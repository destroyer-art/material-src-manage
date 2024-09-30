from app import dbHandler
from sqlalchemy import Column, String
from app.db.dbconnect import Base


class InventorySchema(Base):
    __tablename__ = "Inventory"

    inventory_id = Column(String, primary_key=True)
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
    Location = Column(String, nullable=False)