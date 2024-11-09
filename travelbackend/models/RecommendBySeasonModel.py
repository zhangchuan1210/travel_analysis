# app/models.py
class RecommendBySeason(db.Model):
    __tablename__ = 'recommend_by_season'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    season = db.Column(db.String(50), nullable=False)
    sight = db.Column(db.String(255), nullable=False)
    gone = db.Column(db.Integer, nullable=False)
    wanto = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<RecommendBySeason(season='{self.season}', sight='{self.sight}', gone={self.gone}, wanto={self.wanto})>"
