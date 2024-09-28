from sqlalchemy import Column, String, Numeric

from database.dbconnect import Base


class InventorySchema(Base):
    __tablename__ = "Inventory"

    ID = Column(String, primary_key=True)
    product_number = Column(Numeric, nullable=False)
    material = Column(String, nullable=False)
    form = Column(String, nullable=False)
    choice = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    finish = Column(String, nullable=False)
    surface = Column(String, nullable=True)
    quantity = Column(Numeric, nullable=True)
    weight = Column(Numeric, nullable=False)
    length = Column(Numeric, nullable=True)
    width = Column(Numeric, nullable=True)
    height = Column(Numeric, nullable=True)
    thickness = Column(Numeric, nullable=True)
    outer_diameter = Column(Numeric, nullable=True)
    wall_thickness = Column(Numeric, nullable=True)
    web_thickness = Column(Numeric, nullable=True)
    flange_thickness = Column(Numeric, nullable=True)
    certificates = Column(String, nullable=True)
    Location = Column(String, nullable=False)
