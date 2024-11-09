# app/services/word_count_service.py
from ..models import WordCount
from .. import db

def list_all_word_counts():
    """
    Fetch all records from the WordCount table.
    """
    return db.session.query(WordCount).all()
