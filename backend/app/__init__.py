from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.database.dbconfig import Config
from dotenv import load_dotenv
from sqlalchemy import MetaData

load_dotenv()

app_server = Flask(__name__)
app_server.config.from_object(Config)

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)

dbHandler = SQLAlchemy(app_server, metadata=metadata, engine_options={"pool_pre_ping": True})
migrate = Migrate(app_server, dbHandler)

CORS(app_server, resources={r"/api/*": {"origins": "*", "allow_headers": "*"}})

from app.api.health_api import health_api as health_blueprint

app_server.register_blueprint(health_blueprint)