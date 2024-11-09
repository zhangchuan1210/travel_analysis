# app/controllers/recommend.py
from flask import Blueprint, jsonify, json, make_response
from services.TourismRecommendationService import list_recommendations_by_season

recommend_blueprint = Blueprint('recommend', __name__,url_prefix='/api/recommend')

@recommend_blueprint.route('/recommend', methods=['GET'])
def recommend():
    # Fetch seasonal data
    springs = list_recommendations_by_season("春")
    summers = list_recommendations_by_season("夏")
    autumns = list_recommendations_by_season("秋")
    winters = list_recommendations_by_season("冬")

    # Define lists to hold the "gone" and "want" data by season
    spring_gone, spring_want = [], []
    summer_gone, summer_want = [], []
    autumn_gone, autumn_want = [], []
    winter_gone, winter_want = [], []

    # Grouping lists
    seasons_data = [springs, summers, autumns, winters]
    want_lists = [spring_want, summer_want, autumn_want, winter_want]
    gone_lists = [spring_gone, summer_gone, autumn_gone, winter_gone]

    # Populate "gone" and "want" lists with data
    for i, season_data in enumerate(seasons_data):
        for season_item in season_data:
            # Adding to "gone" list
            gone_entry = {"name": season_item["sight"], "value": season_item["gone"]}
            gone_lists[i].append(gone_entry)

            # Adding to "want" list
            want_entry = {"name": season_item["sight"], "value": season_item["want"]}
            want_lists[i].append(want_entry)

    # Preparing model attributes (similar to adding to the model in Java)
    model = {
        "want": want_lists,
        "gone": gone_lists
    }

    # For demonstration, print the model data
    print("Want Data:", model["want"])
    print("Gone Data:", model["gone"])
    return jsonify(model)

@recommend_blueprint.route('/getData',methods=['POST'])
def getData():
    springs = list_recommendations_by_season("春")
    summers = list_recommendations_by_season("夏")
    autumns = list_recommendations_by_season("秋")
    winters = list_recommendations_by_season("冬")

    # Define lists to hold the "gone" and "want" data by season
    spring_gone, spring_want = [], []
    summer_gone, summer_want = [], []
    autumn_gone, autumn_want = [], []
    winter_gone, winter_want = [], []

    # Combine lists for processing
    seasons_data = [springs, summers, autumns, winters]
    gone_lists = [spring_gone, summer_gone, autumn_gone, winter_gone]
    want_lists = [spring_want, summer_want, autumn_want, winter_want]

    # Populate the "gone" and "want" lists
    for i in range(len(seasons_data)):
        for season_item in seasons_data[i]:
            # "Gone" data
            gone_entry = {
                "name": season_item[0],
                "value": season_item[1]
            }
            gone_lists[i].append(gone_entry)

            # "Want" data
            want_entry = {
                "name": season_item[0],
                "value": season_item[2]
            }
            want_lists[i].append(want_entry)

    # Convert "want" data to JSON format
    want_json = json.dumps(want_lists, ensure_ascii=False)

    # Simulating the HTTP response output
    print(want_json)

    # In a real web app, you'd return want_json as part of the HTTP response.
    # For example:
    response = make_response(want_json)
    response.headers['Content-Type'] = 'application/json;charset=UTF-8'
    return response
