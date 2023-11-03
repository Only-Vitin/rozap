import requests
from random import randint
from bs4 import BeautifulSoup
from utils import send_message
from selenium.common.exceptions import NoSuchElementException

class Suggest():

    def __init__(self, browser, text):
        self.browser = browser
        self.text = text

    def get_random_name(self, type, plataform):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(f'https://www.filmelier.com/br/{type}/{plataform}', headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        atributes = {'class':'title--small'}
        movies = soup.find_all('a', attrs=atributes)
        nmr = randint(0, len(movies))

        movie = movies[nmr].get_text()
        movie_name = str(movie).strip()

        target_a = soup.find(lambda tag: tag.name == 'a' and tag.get_text(strip=True) == movie_name)
        href = target_a['href']

        return movie_name, href

    def open_movie(self):
        href = self.get_random_name('acao', 'netflix')
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.get(href)
        

    def get_url_image(self):
        ...

    def get_description(self):
        ...

    