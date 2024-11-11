# app/models.py
from extensions import db
class Emotion(db.Model):
    __tablename__ = 'emotion'

    id = db.Column(db.Integer, primary_key=True)  # Assuming an ID as the primary key
    words = db.Column(db.String(255), nullable=False)
    positive = db.Column(db.Integer, nullable=False)
    neutral = db.Column(db.Integer, nullable=False)
    negative = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Emotion(words='{self.words}', positive={self.positive}, neutral={self.neutral}, negative={self.negative})>"
