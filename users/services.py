from _tasktracker.mymongodb import MongoDb
from pymongo.errors import ConnectionFailure, DuplicateKeyError
import json

class UserService:

    @classmethod
    def add_user(cls, data):
        db = MongoDb.get_db()
        try:
            users_collection = db['users']
            result = users_collection.insert_one(data)

            return result
        except DuplicateKeyError:
            return {"status": "fail", "message": "User already exists"}
        except Exception as e:
            return {"status": "fail", "message": str(e)}

    