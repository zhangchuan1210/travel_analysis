# app/models.py
from extensions import db
class RecommendBySeason(db.Model):
    __tablename__ = 'recommendseason'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    season = db.Column(db.String(50), nullable=False)
    sight = db.Column(db.String(255), nullable=False)
    gone = db.Column(db.Integer, nullable=False)
    wanto = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<RecommendBySeason(season='{self.season}', sight='{self.sight}', gone={self.gone}, wanto={self.wanto})>"
