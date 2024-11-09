# app/controllers/word_count.py
from flask import Blueprint, jsonify
from ..services.word_count_service import get_word_count

word_count_blueprint = Blueprint('word_count', __name__)

@word_count_blueprint.route('/wordcount', methods=['GET'])
def word_count():
    word_counts = get_word_count()
    return jsonify(word_counts)
