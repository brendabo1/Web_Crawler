import requests
from bs4 import BeautifulSoup
import schedule
from datetime import datetime
import time
from database import Database
from dotenv import load_dotenv
import os

# Site 1: https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc
# Site 2: https://www.adorocinema.com/filmes-todos/


class Crawler:
    def __init__(self):
        load_dotenv()
        self.db = Database()

    """"Requisição na url """
    def request_data(self, url: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_from_IMDb(self):

        raw_data = self.request_data('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc')
        movies = raw_data.find('ul', class_='ipc-metadata-list')

        for movie in movies:
            title = movie.find('h3', class_='ipc-title__text').text
            image = movie.find('img', class_='ipc-image')
            score_users = movie.find('span', class_='ipc-rating-star').text
            link = movie.find('a', class_="ipc-title-link-wrapper")
            data = {
                'title': title,
                'image': image.attrs['src'],
                'score': score_users[0:3], 
                'link': 'https://www.imdb.com' + link.attrs['href'],
                'date': datetime.now()
            }
            print("IMDb", data)
            response = self.db.insert(data)


    def extract_from_adoro_cinema(self, page):
        raw_data = self.request_data(f'https://www.adorocinema.com/filmes-todos/?{page}')
        movies = raw_data.find_all('li', class_='mdl')
        for movie in movies:
            title = movie.find('h2', class_='meta-title').text.strip("\n")

            image = movie.find('img', class_='thumbnail-img')
            score_users = movie.find('span', class_='stareval-note').text
            link = movie.find('a', class_="meta-title-link")
            data = {
                'title': title,
                'image': image.attrs['src'],
                'score': score_users, 
                'link': 'https://www.adorocinema.com' + link.attrs['href'],
                'date': datetime.now()
            }
            response = self.db.insert(data)
            print("AdoroCinema", data)

    def execute_adoro_cinema(self, num_pages: int = 3):
        for page in range(1, num_pages):
            self.extract_from_adoro_cinema(page)
            exit()
            
    

# Permite a execução do código apenas quando este arquivo é executado diretamente, e não quando importado
if __name__=="__main__":
    crawler = Crawler()

    print("\n Execute job. Time: {}".format(str(datetime.now())))
    crawler.extract_from_IMDb()
    crawler.execute_adoro_cinema(3)
    
    # def execute(num_pages = 3):
    #     print("\n Execute job. Time: {}".format(str(datetime.now())))
    #     crawler.extract_from_IMDb()
    #     crawler.execute_adoro_cinema(num_pages)
    
    # schedule.every(5).minutes.do(execute())

    # while True:
    #     schedule.run_pending()