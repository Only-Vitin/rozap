import requests
from unidecode import unidecode
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import send_message
from storage_files import streamings, genres


class Suggest():

    def __init__(self, browser, text):
        self.browser = browser
        self.text = text
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}

    def get_random_href(self, url):
        page = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        atributes = {'class':'title-list-grid__item--link'}
        movies = soup.find_all('a', attrs=atributes)
        nmr = randint(0, len(movies))

        random_a = movies[nmr]
        href = str(random_a['href'])
        href = f"https://www.justwatch.com{href}"

        print(href)
        return href
          
    def get_image_src(self, href):   
        page = requests.get(href, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        picture = soup.find('picture', class_='picture-comp title-poster__image')
        atributes = {'type':'image/webp'}
        img_tag = picture.find('source', attrs=atributes)

        src = str(img_tag['data-srcset'])
        return src
    
    def get_description(self, href):
        page = requests.get(href, headers=self.headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        #name and date
        atributes = {'class':'title-block'}
        title = soup.find('div', attrs=atributes)
        name = title.find('h1').get_text()
        date = title.find('span').get_text()

        #streamings
        atributes = {'class':'buybox-row stream'}
        streamings = soup.find('div', attrs=atributes)

        try:
            atributes = {'class':'offer__icon'}
            streaming_img = streamings.find('img', attrs=atributes)
            streaming_name = str(streaming_img['alt'])
        except AttributeError:
            streaming_name = "Não está disponível para streaming"

        #sinopse
        try:
            atributes = {'class':'article-block'}
            article = soup.find('article', attrs=atributes)

            atributes = {'dir':'ltr'}
            sinopse = article.find('p', attrs=atributes).get_text()
        except AttributeError:
            atributes = {'class':'text-wrap-pre-line mt-0'}
            sinopse = soup.find('p', attrs=atributes).get_text()

        if len(sinopse) > 250:
            sinopse = f"{sinopse[:250]}..."

        description = f"Nome: *{name.strip()}* - {date.strip()}\n\nDisponível no(a): {streaming_name.strip()}\n\nSinopse: \n{sinopse}\n\nFonte: {href}"
        return description

    def copy_paste_image(self, src, message):
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.get(src)
        
        image = self.browser.find_element(By.XPATH, "//img[contains(@style, 'display')]")
        
        actions = ActionChains(self.browser)
        actions.move_to_element(image)
        
        actions.key_down(Keys.CONTROL)
        actions.send_keys('c')
        actions.key_up(Keys.CONTROL)
        actions.perform()
        
        self.browser.switch_to.window(self.browser.window_handles[0])
    
        text_box = self.browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
        text_box.click()
        text_box.send_keys(Keys.CONTROL, 'v')
        
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class*='ppled2lx ln8gz9je'] p[class*='copyable-text']")))

        text_box_on_img = self.browser.find_element(By.CSS_SELECTOR, "div[class*='ppled2lx ln8gz9je'] p[class*='copyable-text']")
        text_box_on_img.click()
    
        lines = message.split("\n")
        for line in lines:
            text_box_on_img.send_keys(line)
            text_box_on_img.send_keys(Keys.SHIFT, Keys.ENTER)
        
        send_button = self.browser.find_element(By.CSS_SELECTOR, "div[class*='ppled2lx ln8gz9je'] div[aria-label='Enviar']")
        send_button.click()
        sleep(3)

    def suggest(self):
        url = "https://www.justwatch.com/br"
        text = self.text
        text.pop(0)
        for par in text:
            par = unidecode(par.lower().strip())
            if par in streamings:
                url = f"{url}/provedor/{par}"

            elif par in ['filmes', 'series']:
                url = f"{url}/{par}"

            elif par in genres:
                genre_code = genres[par]
                url = f"{url}?genres={genre_code}"

            else:
                send_message(self.browser, f"Erro no parametro: {par}")
                return 0
        href = self.get_random_href(url)
        src = self.get_image_src(href)
        message = self.get_description(href)
        self.copy_paste_image(src, message)
        