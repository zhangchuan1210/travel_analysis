# app/models.py
from extensions import db

class ProvinceHotModel(db.Model):
    __tablename__ = 'province_hot'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    province = db.Column(db.String(100), nullable=False)
    hotspot = db.Column(db.BigInteger, nullable=False)

    def __repr__(self):
        return f"<ProvinceHot(province='{self.province}', hotspot={self.hotspot})>"
