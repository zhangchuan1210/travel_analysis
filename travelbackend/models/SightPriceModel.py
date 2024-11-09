# app/models.py
class SightPrice(db.Model):
    __tablename__ = 'sight_price'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    city = db.Column(db.String(100), nullable=False)
    avg_price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<SightPrice(city='{self.city}', avg_price={self.avg_price})>"
