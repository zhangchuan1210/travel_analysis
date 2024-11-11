# app/services/city_service.py
from models.CityModel import CityModel
from extensions import db

def list_all_cities():
    """
    Fetch all records from the City table.
    """
    return db.session.query(CityModel).all()
