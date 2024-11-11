# app/services/province_hot_service.py
from models.ProvinceHotModel import ProvinceHotModel
from extensions import db

def list_all_province_hot():
    """
    Fetch all records from the ProvinceHot table.
    """
    return db.session.query(ProvinceHotModel).all()
