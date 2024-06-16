# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
#import os
import sqlite3



#engine = create_engine(data_base)
#local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sqlite3.connect("database/data.sqlite")
    return db