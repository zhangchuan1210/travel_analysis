# app/models.py
from extensions import db

class CityModel(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    city = db.Column(db.String(100), nullable=False)
    lng = db.Column(db.Float, nullable=False)
    lat = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<City(city='{self.city}', lng={self.lng}, lat={self.lat})>"
