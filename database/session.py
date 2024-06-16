# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


local_path = os.path.dirname(os.path.abspath(__file__))
data_base = rf"sqlite:///{local_path}data.sqlite"

engine = create_engine(data_base)
local_session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = local_session()
    try:
        yield db
    finally:
        db.close()