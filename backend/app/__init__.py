from flask import Flask
from flask_cors import CORS

from app.api.health_api import health_api as health_blueprint

app_server = Flask(__name__)
CORS(app_server, resources={r"/api/*": {"origins": "*", "allow_headers": "*"}})

app_server.register_blueprint(health_blueprint)
