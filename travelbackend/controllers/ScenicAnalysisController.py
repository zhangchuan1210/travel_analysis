# app/controllers/tickets.py
from flask import Blueprint, jsonify
from services.tickets_service import get_tickets

tickets_blueprint = Blueprint('tickets', __name__,url_prefix='/api/travel')

@tickets_blueprint.route('/tickets', methods=['GET'])
def tickets():
    tickets = get_tickets()
    return jsonify(tickets)
