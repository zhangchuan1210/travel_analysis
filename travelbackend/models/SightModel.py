# app/models.py
class Sight(db.Model):
    __tablename__ = 'sight'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    city_name = db.Column(db.String(100), nullable=False)
    counts = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Sight(city_name='{self.city_name}', counts={self.counts})>"
