import csv
from database.dbconnect import SessionLocal
from database.schemas.Inventory import InventorySchema

dbHandler = SessionLocal()


async def load_inventory_info():
    with open("data/inventory.csv", mode="r") as file:
        inventory_data = csv.DictReader(file)
        column_names = file.readline().strip().split(",")

        for data in inventory_data:
            new_inventory = InventorySchema(
                product_number=data[column_names[0]],
                material=data[column_names[1]],
                form=data[column_names[2]],
                choice=data[column_names[3]],
                grade=data[column_names[4]],
                finish=data[column_names[5]],
                surface=data[column_names[6]],
                quantity=data[column_names[7]],
                weight=data[column_names[8]],
                length=data[column_names[9]],
                width=data[column_names[10]],
                height=data[column_names[11]],
                thickness=data[column_names[12]],
                outer_diameter=data[column_names[13]],
                wall_thickness=data[column_names[14]],
                web_thickness=data[column_names[15]],
                flange_thickness=data[column_names[16]],
                certificates=data[column_names[17]],
                Location=data[column_names[19]],
            )
            dbHandler.add(new_inventory)
            await dbHandler.commit()
            await dbHandler.refresh()

    print("All inventory data was inserted")
