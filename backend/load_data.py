import csv
from app import dbHandler, app_server
from app.database.schemas.Inventory import InventorySchema

async def load_inventory_info():
    with open("data/inventory.csv", mode="r") as file:
        column_names = file.readline().strip().split(",")
        print (column_names)
        inventory_data = csv.reader(file)

        with app_server.app_context():
            for data in inventory_data:
                for dt in data:
                    print (type(dt))
                new_inventory = InventorySchema(
                    product_number=data[0],
                    material=data[1],
                    form=data[2],
                    choice=data[3],
                    grade=data[4],
                    finish=data[5],
                    surface=data[6],
                    quantity=data[7],
                    weight=data[8],
                    length=data[9],
                    width=data[10],
                    height=data[11],
                    thickness=data[12],
                    outer_diameter=data[13],
                    wall_thickness=data[14],
                    web_thickness=data[15],
                    flange_thickness=data[16],
                    certificates=data[17],
                    Location=data[18],
                )
                dbHandler.session.add(new_inventory)
                dbHandler.session.commit()

    print("All inventory data was inserted")
