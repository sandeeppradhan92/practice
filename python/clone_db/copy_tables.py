
import sys
from sqlalchemy import MetaData, Table, inspect
from sqlalchemy.ext.declarative import declarative_base

from create_db_connection import db_connection

connection_params = {'drivername': 'postgres',
               'username': 'postgres',
               'password': 'postgres',
               'host': 'localhost',
               'port': 5432} 

def make_session(connection_params):
    conn = db_connection(connection_params)
    engine = conn.engine
    session = conn.session
    return session, engine

def run():
    source, sengine = make_session(connection_params)
    smeta = MetaData(bind=sengine)
    # destination, dengine = make_session(to_db)

    # Get table information
    inspector = inspect(sengine)
    table_list = inspector.get_table_names()

    for table_name in table_list:
        print('Processing', table_name)
        print('Pulling schema from source server')
        table = Table(table_name, smeta, autoload=True)   
        print(table)
        # pull_table_structure(table, dengine) 
        # pull_table_data(table, dengine, source, destination)
        
    print('Committing changes')
    # destination.commit()


def pull_table_structure(table, engine):
    print('Creating table on destination server')
    table.metadata.create_all(engine)

# def pull_table_data(table, engine, source, destination):
#     NewRecord = quick_mapper(table)
#     columns = table.columns.keys()
#     print('Transferring records')
#     for record in source.query(table).all():
#         data = dict(
#             [(str(column), getattr(record, column)) for column in columns]
#         )
#         destination.merge(NewRecord(**data))

def print_usage():
    print("""TBD""") 

# def quick_mapper(table):
#     Base = declarative_base()
#     class GenericMapper(Base):
#         __table__ = table
#     return GenericMapper

if __name__ == '__main__':
    run()