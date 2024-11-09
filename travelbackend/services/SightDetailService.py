# app/services/sight_details_service.py
from ..models import SightDetails
from .. import db
from sqlalchemy.sql import text

def find_sights_by_city_name(city_name):
    """
    Fetch sight details based on the city name.
    """
    return db.session.query(SightDetails).filter(SightDetails.city_name == city_name).all()

def list_by_sql_return_entity(sql):
    """
    Execute a raw SQL query and return the results.
    """
    return db.session.execute(text(sql)).fetchall()
