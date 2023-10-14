import requests
from bs4 import BeautifulSoup
import json

# Site 1: https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc
# Site 2: https://www.adorocinema.com/filmes-todos/


class Crawler:

    """"Faz a requisição na url """
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
            title = movie.find('h3', class_='ipc-title__text')
            #title = json.loads(title)['title']
            #image 
            #score_users 
            #link

            #second_request = self.request_data(link)

            data = {
                #'image': image.attrs['data-src'],
                'title': title,
                #'link': link
                
            }
            print(data)
            
            break


    def extract_from_adoro_cinema(self):
        raw_data = self.request_data('https://www.adorocinema.com/filmes-todos/')
        filmes =  raw_data.findAll('h2', {'class': 'meta-title'})


# Permite a execução do código apenas quando este arquivo é executado diretamente, e não quando importado
if __name__=="__main__":
    crawler = Crawler()
    crawler.extract_from_IMDb()