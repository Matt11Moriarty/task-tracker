import os
from pymongo import MongoClient

class MongoDb:
    
    connection_string = os.getenv("CLUSTER_CONNECTION_STRING")
    db_name = os.getenv("DB_NAME")

    def get_db(self):
        client = MongoClient(self.connection_string)
        db = client[self.db_name]
        if db is None:
            raise ValueError("Failed to connect to the database")
        return db
