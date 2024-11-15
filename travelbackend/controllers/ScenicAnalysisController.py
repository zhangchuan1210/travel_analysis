# app/controllers/tickets.py
from flask import Blueprint, jsonify
from services.ScenicAnalysisService import get_tickets

tickets_blueprint = Blueprint('tickets', __name__,url_prefix='/api/tickets')

@tickets_blueprint.route('/listtickets', methods=['GET'])
def tickets():
    tickets = get_tickets()
    return jsonify(tickets)
