# database/session.py
import sqlite3


def get_db():
    db = sqlite3.connect("database/data.sqlite")
    return db