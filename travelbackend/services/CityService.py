# app/services/city_service.py
from ..models import City
from .. import db

def list_all_cities():
    """
    Fetch all records from the City table.
    """
    return db.session.query(City).all()
