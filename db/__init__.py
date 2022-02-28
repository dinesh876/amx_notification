import os
from functools import lru_cache
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


@lru_cache(maxsize=32)
def engine(db_url=None):
    db_url = db_url or os.getenv("DB_URL")
    if not db_url:
        raise ValueError(" database URL is required")
    return create_engine(db_url)


def get_connection(db_url=None):
    return engine(db_url)

@lru_cache(maxsize=32)
def session_class(db_url=None):
    return sessionmaker(bind=engine(db_url))

try:
    HOST = "10.221.86.73"
    USERNAME = "root"
    PASSWORD = "Ttpl@123"
    DATABASE = "cdr_database"
    db_url = "pymysql://{}:{}@{}:3306/{}".format(USERNAME, PASSWORD,HOST,DATABASE)
    Session = session_class(db_url)
except:
    pass

#db = get_connection()
#results = db.execute("select * from users where id=1")
#result = [dict(row) for row in results.fetchall()]
#print(result)