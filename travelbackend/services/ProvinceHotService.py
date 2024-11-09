# app/services/province_hot_service.py
from ..models import ProvinceHot
from .. import db

def list_all_province_hot():
    """
    Fetch all records from the ProvinceHot table.
    """
    return db.session.query(ProvinceHot).all()
