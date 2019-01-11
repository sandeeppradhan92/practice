from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class db_connection:
    def __init__(self, conn_parameters):
        self.conn_parameters = conn_parameters
        connection_string = URL(**conn_parameters)
        self._engine = create_engine(connection_string, echo=False, convert_unicode=True)        
        self._session = sessionmaker(bind=self._engine)()

    def __repr__(self):
        return "{drivername} connection object for {host}:{port}".format(
            self.conn_parameters
        )

    @property
    def engine(self):
        return self._engine

    @property
    def session(self):
        return self._session

    def close_conn(self):
        self._session.close()
        self._engine.close()


