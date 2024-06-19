import os
from pymongo import MongoClient

class MongoDb:
    
    connection_string = os.getenv("CLUSTER_CONNECTION_STRING")
    db_name = os.getenv("DB_NAME")

    @classmethod
    def get_db(cls):
        client = MongoClient(cls.connection_string)
        db = client[cls.db_name]
        if db is None:
            raise ValueError("Failed to connect to the database")
        return db
