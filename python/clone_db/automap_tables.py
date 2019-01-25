from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL

Base = automap_base()

# engine set up
postgres_db = {'drivername': 'postgres',
               'username': 'postgres',
               'password': 'postgres',
               'host': 'localhost',
               'port': 5432}    

db_string = URL(**postgres_db)
engine = create_engine(db_string)

# reflect the tables
Base.prepare(engine, reflect=True)

tables = {}

for item in Base.classes.items():
    tables[item[0].title()] = item[1]

from pprint import pprint as print

print(tables)