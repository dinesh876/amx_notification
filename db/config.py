from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote
from properties import DB_PASSWORD,DB_USERNAME,DB_HOST,DB_PORT,DATABASE


@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url 
    if not db_url:
        raise ValueError(" database URL is required")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url)

@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))

try:
    HOST = DB_HOST
    USERNAME = quote(DB_USERNAME)
    PASSWORD = quote(DB_PASSWORD)
    DB  = DATABASE
    PORT = DB_PORT
    DB_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(USERNAME,PASSWORD,HOST,PORT,DB)
    Session = session_class(DB_URL)
except:
    pass
