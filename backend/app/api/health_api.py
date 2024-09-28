from flask import Blueprint, jsonify

health_api = Blueprint("health", __name__)


@health_api.route("/health", methods=["GET"])
def health_check():
    return jsonify({"Status": "OK", "Message": "Server is running!"})
