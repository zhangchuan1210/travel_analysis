from sqlalchemy import text

import services.ProvinceHotService as ProvinceHot
import services.SightDetailService as SightDetails
from extensions import db
from flask import jsonify
def get_province_hot():
    province_hot_list = ProvinceHot.list_all_province_hot()
    data_list = [{'name': ph.province, 'value': ph.hotspot} for ph in province_hot_list]

    # Query for popular sights in each city
    cities = SightDetails.find_sights_by_city_name()
    popular_sights = []
    for city in cities:
        city_id = city.city_id
        city_name=city.city_name
        sql="select * from sight_detail where city_id='"+city_id+"' and comment_num>500"
        sights = SightDetails.list_by_sql_return_entity(sql)
        for sight in sights:
            popular_sights.append({'city': city_name, 'sight_id': sight.sight_id})

    return jsonify({'province_data': data_list, 'popular_sights': popular_sights})