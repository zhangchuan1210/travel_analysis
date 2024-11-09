# app/controllers/hotspot.py
from flask import Blueprint, jsonify
from ..models import ProvinceHot, SightDetails
from .. import db

hotspot_blueprint = Blueprint('hotspot', __name__)

@hotspot_blueprint.route('/hotspot', methods=['GET'])
def get_province_hot():
    # Fetch province hotspot data
    province_hot_list = ProvinceHot.query.all()
    data_list = [{'name': ph.province, 'value': ph.hotspot} for ph in province_hot_list]

    # Query for popular sights in each city
    cities = db.session.query(SightDetails.city_name).distinct().all()
    popular_sights = []
    for city in cities:
        city_name = city[0]
        sights = SightDetails.query.filter(SightDetails.city_name == city_name, SightDetails.comment_num > 500).all()
        for sight in sights:
            popular_sights.append({'city': city_name, 'sight_id': sight.id})

    return jsonify({'province_data': data_list, 'popular_sights': popular_sights})
