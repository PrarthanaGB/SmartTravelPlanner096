from flask import Blueprint, request, jsonify
from utils.ai_helper import generate_itinerary

ai_bp = Blueprint('ai_bp', __name__)

@ai_bp.route('/ai', methods=['POST'])
def ai_recommendation():
    data = request.get_json()
    place = data.get('place')
    days = data.get('days')
    budget = data.get('budget')
    transport = data.get('transport')

    itinerary = generate_itinerary(place, days, budget, transport)
    return jsonify(itinerary)