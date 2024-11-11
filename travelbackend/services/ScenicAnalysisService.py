import json
import services.SightPriceService as SightPriceService
import services.CityService as CityService
import services.ProvinceHotService as ProvinceService
def get_tickets():
    # Process sightseeing prices
    price_list = SightPriceService.list_all_sight_prices()
    prices = []
    for sight_price in price_list:
        price_map = {
            "name": sight_price.city,
            "value": sight_price.avg_price
        }
        prices.append(price_map)

    # Process city geographic locations
    city_list = CityService.list_all_cities()
    city_map = {}
    for city in city_list:
        loc = [city.lng, city.lat]
        city_map[city.city] = loc
    city_json = json.dumps(city_map)

    # Process sightseeing popularity data
    province_hot_list = ProvinceService.list_all_province_hot()
    data_list = []
    for province_hot in province_hot_list:
        province_hot_map = {
            "name": province_hot.province,
            "value": province_hot.hotspot
        }
        data_list.append(province_hot_map)

    # Price range statistics data
    price_sql = "SELECT avg_price FROM sight_price WHERE city <> '山南'"
    price_num = SightPriceService.get_prices_by_sql(price_sql)

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
        count = SightPriceService.get_count_by_sql(sql)
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
    return context
