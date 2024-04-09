from flask import Blueprint, request, jsonify
from src.database import DB
from src.logger import logger

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/auth/register', methods=['POST'])
def receive_auth_registration():
    vehicle_id = request.json['vehicle_id']

    token = DB.create_token(vehicle_id)

    token_data = {
        "token": token
    }

    logger.info('Created token vehicle_id: %s', vehicle_id)
    return jsonify(token_data), 201


def authenticate_token(token):
    token_data = DB.get_token(token)

    if not token_data:
        return None

    return token_data[0][1]
