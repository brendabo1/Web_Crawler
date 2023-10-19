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
            print("Filme salvo com sucesso", data)
            return movie      
        else:
            return None

if __name__=="__main__":
    # print
    db = Database()
    #result = db.movies.delete_many({})
    var1 = {'title': 'O Lobo de Wall Street', 'image': 'https://m.media-amazon.com/images/M/MV5BZTk1Y2ViODktYjc5Mi00MTQwLWI1ZjItODQwYmI1NDQzMDU0XkEyXkFqcGdeQXVyODc0OTEyNDU@._V1_QL75_UY207_CR1,0,140,207_.jpg', 'score': 8.2, 'link': 'https://www.imdb.com/title/tt0993846/?ref_=chtmvm_t_86', 'date': datetime.now()}
    db.insert(var1)
    
    