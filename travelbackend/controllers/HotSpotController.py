# app/controllers/hotspot.py
from flask import Blueprint, jsonify
import services.HotSpotService as hotSpotService

hotspot_blueprint = Blueprint('hotspot', __name__,url_prefix='/api/hotspot')

@hotspot_blueprint.route('/listhotspot', methods=['GET'])
def get_province_hot():
    # Fetch province hotspot data
    province_hot_list =hotSpotService.get_province_hot()
    return province_hot_list