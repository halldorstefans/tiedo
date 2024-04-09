from flask import Blueprint, request, jsonify
from src.database import DB
from src.auth import authenticate_token
from src.logger import logger

gps_bp = Blueprint('gps', __name__)


# API Endpoint to receive GPS data from vehicles
@gps_bp.route('/api/gps', methods=['POST'])
def receive_gps_data():
    token = request.headers.get('Authorization')

    auth_vehicle_id = authenticate_token(token)

    if auth_vehicle_id is None:
        logger.warning('Unauthorized access to /api/gps')
        return jsonify({"error": "Unauthorized"}), 401

    vehicle_id = DB.receive_gps_data(request.json)

    if vehicle_id != auth_vehicle_id:
        logger.warning('Unauthorized access for the vehicle')
        return jsonify({"error": "Unauthorized"}), 401

    logger.info('Received GPS data for vehicle_id: %s', vehicle_id)
    return jsonify({"message": "GPS data received and saved"}), 201


# API Endpoint to retrieve GPS data for a specific vehicle
@gps_bp.route('/api/gps/<vehicle_id>', methods=['GET'])
def get_gps_data(vehicle_id):
    token = request.headers.get('Authorization')

    auth_vehicle_id = authenticate_token(token)

    if auth_vehicle_id is None:
        logger.warning('Unauthorized access to /api/gps')
        return jsonify({"error": "Unauthorized"}), 401

    if vehicle_id != auth_vehicle_id:
        logger.warning('Unauthorized access for the vehicle')
        return jsonify({"error": "Unauthorized"}), 401

    data = DB.get_gps_data(vehicle_id)

    if not data:
        logger.warning('No GPS data found for vehicle_id: %s', vehicle_id)
        return jsonify({"error": "No GPS data found for the vehicle"}), 404

    gps_data = []
    for row in data:
        gps_data.append({
            "id": row[0],
            "vehicle_id": row[1],
            "timestamp": row[2],
            "latitude": row[3],
            "longitude": row[4]
        })

    logger.info('Retrieved GPS data for vehicle_id: %s', vehicle_id)
    return jsonify({"gps_data": gps_data}), 200
