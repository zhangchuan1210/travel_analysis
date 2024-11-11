# app/models.py
from extensions import db

class WordCount(db.Model):
    __tablename__ = 'word_count'

    index = db.Column(db.BigInteger, primary_key=True)  # Using `index` as the primary key
    word = db.Column(db.String(255), nullable=False)
    count = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<WordCount(word='{self.word}', count={self.count})>"
