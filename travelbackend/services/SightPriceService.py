# app/services/sight_price_service.py
from models.SightPriceModel import SightPriceModel
from extensions import db
from sqlalchemy.sql import text

def list_all_sight_prices():
    """
    Fetch all records from the SightPrice table.
    """
    return db.session.query(SightPriceModel).all()

def get_prices_by_sql(sql):
    """
    Execute a raw SQL query and return a list of prices.
    """
    result = db.session.execute(text(sql)).fetchall()
    return [row[0] for row in result]

def get_count_by_sql(sql):
    """
    Execute a raw SQL query to get a count.
    """
    result = db.session.execute(text(sql)).scalar()
    return result if result else 0
