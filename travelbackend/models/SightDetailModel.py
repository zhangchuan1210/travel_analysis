# app/models.py
from extensions import db

class SightDetails(db.Model):
    __tablename__ = 'sight_details'

    rowid = db.Column(db.Integer, primary_key=True)
    city_name = db.Column(db.String(100), nullable=False)
    city_id = db.Column(db.String(50), nullable=False)
    sight_id = db.Column(db.String(50), nullable=False)
    sight_name = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Float, nullable=False)
    comment_num = db.Column(db.Integer, nullable=False)
    rank = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<SightDetails(city_name='{self.city_name}', sight_name='{self.sight_name}', score={self.score})>"
