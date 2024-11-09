import json
import services.SightPriceService

def get_tickets():
    # Process sightseeing prices
    price_list = new SightPriceService().list_all()
    prices = []
    for sight_price in price_list:
        price_map = {
            "name": sight_price.city,
            "value": sight_price.avg_price
        }
        prices.append(price_map)

    # Process city geographic locations
    city_list = cityService.list_all()
    city_map = {}
    for city in city_list:
        loc = [city.lng, city.lat]
        city_map[city.city] = loc
    city_json = json.dumps(city_map)

    # Process sightseeing popularity data
    province_hot_list = provinceHotService.list_all()
    data_list = []
    for province_hot in province_hot_list:
        province_hot_map = {
            "name": province_hot.province,
            "value": province_hot.hotspot
        }
        data_list.append(province_hot_map)

    # Price range statistics data
    price_sql = "SELECT avg_price FROM sight_price WHERE city <> '山南'"
    price_num = sightPriceService.get_by_sql_return_price(price_sql)

    # Count of cities by price ranges
    count_ranges_sql = [
        ("0-50", "SELECT COUNT(city) FROM sight_price WHERE avg_price <= 50"),
        ("50-100", "SELECT COUNT(city) FROM sight_price WHERE avg_price > 50 AND avg_price <= 100"),
        ("100-200", "SELECT COUNT(city) FROM sight_price WHERE avg_price > 100 AND avg_price <= 200"),
        ("200-300", "SELECT COUNT(city) FROM sight_price WHERE avg_price > 200 AND avg_price <= 300"),
        ("300- ", "SELECT COUNT(city) FROM sight_price WHERE avg_price > 300")
    ]
    count_list = []
    for tag, sql in count_ranges_sql:
        count = sightPriceService.get_count(sql)
        count_map = {
            "name": tag,
            "value": count
        }
        count_list.append(count_map)

    # Context for rendering
    context = {
        "countList": count_list,
        "priceNum": price_num,
        "datalist": data_list,
        "cityJson": city_json,
        "prices": prices
    }
