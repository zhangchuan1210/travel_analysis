# app/controllers/recommend.py
from flask import Blueprint, jsonify
from ..services.recommend_service import get_recommendations

recommend_blueprint = Blueprint('recommend', __name__)

@recommend_blueprint.route('/recommend', methods=['GET'])
def recommend():
    recommendations = get_recommendations()
    return jsonify(recommendations)
