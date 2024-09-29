import asyncio
from app import app_server, dbHandler
from load_data import load_inventory_info

if __name__ == "__main__":
    asyncio.run(load_inventory_info())
    # load_inventory_info()
    with app_server.app_context():
        try:
            dbHandler.create_all()
        except Exception as e:
            print ("DB initialize failed!")
            pass
    app_server.run(debug=False, port=5000)
