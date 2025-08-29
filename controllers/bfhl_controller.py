from flask import Blueprint, request, jsonify
from services.data_service import process_data
from models.user_model import get_user_info

bfhl_bp = Blueprint("bfhl", __name__)

@bfhl_bp.route('bfhl', methods=['POST'])
def bfhl_route():
    try:
        data = request.get_json()
        array = data.get("data", [])

        user = get_user_info()

  
        result = process_data(array, user)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400
