# app/services/sight_details_service.py
from models.SightDetailModel import SightDetails
from extensions import db
from sqlalchemy.sql import text

def find_sights_by_city_name():
    """
    Fetch sight details based on the city name.
    """
    return db.session.query(SightDetails).distinct().all()

def list_by_sql_return_entity(sql):
    """
    Execute a raw SQL query and return the results.
    """
    return db.session.execute(text(sql)).fetchall()
