# controllers/scraper_controller.py
from flask import Blueprint, jsonify, request

from services.travel_service import TravelService

scraper_bp = Blueprint('travel', __name__, url_prefix='/travel')
travelService=TravelService()
@scraper_bp.route('/scrape/places', methods=['GET'])
def scrapePlaces():
    travelService.get_place(url=request.args.get('url'))
    return jsonify({'message': 'Data scraped successfully!'})
@scraper_bp.route('/scrape/info',methods=['GET'])
def scrapeTravel():
    id_ca = travelService.get_place(url=request.args.get('url'))
    # id_ca=[['hangzhou14']]
    for i in range(0, len(id_ca)):
        city_id = id_ca[i]
        print(city_id)
        for city_id3 in city_id:
            print(city_id3)
            url_4 = 'https://you.ctrip.com/sight/' + city_id3 + '.html'
            travelService.get_sight_info(url_4)
            url_5 = 'https://you.ctrip.com/sight/' + city_id3 + '/s0-p2.html'
    return jsonify({'message': 'Data scraped successfully!'})
