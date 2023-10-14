import requests
from bs4 import BeautifulSoup

# Site 1: https://www.adorocinema.com/filmes-todos/
# Site 2: RottenTomatoes https://www.rottentomatoes.com/browse/movies_at_home/audience:upright~critics:certified_fresh~sort:popular
#https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc

#Checagem da possibilidade de scrapping

import random

# user_agents_list = [
#     'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
# ]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}
r = requests.get('https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc', headers=headers)

#response = requests.get("https://filmow.com/filmes-todos/")
#response = requests.get("https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm&sort=rank%2Casc")

soup = BeautifulSoup(r.text, 'html.parser')


title = soup.findAll('h3', {'class': 'ipc-title__text'})
for item in title:
    print(item.text)

#score = soup.find('span', {'class': 'stareval-note'})
#score = soup.find('span', 'aria-label')

# filme =  soup.findAll('h2', {'class': 'meta-title'})
#filme =  soup.find('span', {'data-qa': 'audience-score'})
#data_link = soup.find('a', {'data-qa': 'discovery-media-list-item-caption'})


