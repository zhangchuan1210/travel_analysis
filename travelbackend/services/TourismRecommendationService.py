# app/services/recommend_by_season_service.py
from models.RecommendBySeason import RecommendBySeason
from extensions import db
from sqlalchemy import text


def list_recommendations_by_season(season):
    """
    Fetch recommendations based on the season.
    """
    query = text("SELECT sight, gone, wanto FROM recommend_by_season WHERE season = :season")
    result = db.session.execute(query, {"season": season}).fetchall()
    return result
    #return db.session.query(RecommendBySeason).filter(RecommendBySeason.season == season).all()
