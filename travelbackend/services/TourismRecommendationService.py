# app/services/recommend_by_season_service.py
from ..models import RecommendBySeason
from .. import db

def list_recommendations_by_season(season):
    """
    Fetch recommendations based on the season.
    """
    return db.session.query(RecommendBySeason).filter(RecommendBySeason.season == season).all()
