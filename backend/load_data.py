import csv

def load_inventory_info():
    with open("data/inventory.csv", mode="r") as file:
        inventory_data = csv.DictReader(file)
        column_names = file.readline().strip().split(',')
        
