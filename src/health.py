from flask import Blueprint, jsonify
from src.database import DB
from src.logger import logger

health_bp = Blueprint('health', __name__)

# Configure health check
is_healthy = False


@health_bp.route('/health', methods=['GET'])
def health_check():
    is_healthy = DB.verify_schema()

    if is_healthy:
        logger.info('Health check passed')
        return jsonify({"status": "Healthy"}), 200
    else:
        logger.error('Health check failed')
        return jsonify({"status": "Unhealthy"}), 500
