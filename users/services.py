from _tasktracker.mymongodb import MongoDb
from pymongo.errors import ConnectionFailure, DuplicateKeyError

class UserService:

    def add_user(data):
        db = MongoDb.get_db()
        try:
            users_collection = db['users']
            result = users_collection.insert_one(data)
            return {
                "status": "success",
                "inserted_id": "{data.id}"
            }
        except DuplicateKeyError:
            return {"status": "fail", "message": "User already exists"}
        except Exception as e:
            return {"status": "fail", "message": str(e)}

    