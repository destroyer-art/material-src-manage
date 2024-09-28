from app import app_server
from dotenv import load_dotenv
from load_data import load_inventory_info

if __name__ == "__main__":
    load_dotenv()

    load_inventory_info()
    app_server.run(debug=False, port=5000)
