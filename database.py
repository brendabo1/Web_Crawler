from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
from datetime import datetime

class Database:
    
    def __init__(self) -> None:
        load_dotenv()
        self.movies = self.connect()

    def connect(self):
        client = MongoClient(os.getenv('DB_URI'))
        db = client['movies']
        return db.movies 
    
   #------------ Comparativo ------------------
    def insert(self, data: dict):
        query = {'title': data['title']}
        result = self.movies.find_one(query, sort=[('date', -1)])
        if result is None:
            self.movies.insert_one(data)
            return data
        elif result['score'] > data['score'] or result['score'] < data['score']:
            movie = data.copy()
            movie['old_score'] = result['score']
            self.movies.insert_one(data)
    
            return movie      
        else:
            return None

if __name__=="__main__":
    
    db = Database()
    #result = db.movies.delete_many({})
    