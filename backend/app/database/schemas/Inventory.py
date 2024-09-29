from app import dbHandler
from sqlalchemy import String


class InventorySchema(dbHandler.Model):
    __tablename__ = "Inventory"

    inventory_id = dbHandler.Column(String, primary_key=True)
    product_number = dbHandler.Column(String, nullable=False)
    material = dbHandler.Column(String, nullable=False)
    form = dbHandler.Column(String, nullable=False)
    choice = dbHandler.Column(String, nullable=False)
    grade = dbHandler.Column(String, nullable=False)
    finish = dbHandler.Column(String, nullable=False)
    surface = dbHandler.Column(String, nullable=True)
    quantity = dbHandler.Column(String, nullable=True)
    weight = dbHandler.Column(String, nullable=False)
    length = dbHandler.Column(String, nullable=True)
    width = dbHandler.Column(String, nullable=True)
    height = dbHandler.Column(String, nullable=True)
    thickness = dbHandler.Column(String, nullable=True)
    outer_diameter = dbHandler.Column(String, nullable=True)
    wall_thickness = dbHandler.Column(String, nullable=True)
    web_thickness = dbHandler.Column(String, nullable=True)
    flange_thickness = dbHandler.Column(String, nullable=True)
    certificates = dbHandler.Column(String, nullable=True)
    Location = dbHandler.Column(String, nullable=False)
