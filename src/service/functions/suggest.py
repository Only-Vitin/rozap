import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Suggest():

    def __init__(self, browser, text):
        self.browser = browser
        self.text = text

    def get_random_name_href(self, type, plataform):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(f'https://www.filmelier.com/br/{type}/{plataform}', headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        atributes = {'class':'title--small'}
        movies = soup.find_all('a', attrs=atributes)
        nmr = randint(0, len(movies))

        movie = movies[nmr].get_text()
        movie_name = str(movie).strip()

        target_a = soup.find(lambda tag: tag.name == 'a' and tag.get_text(strip=True) == movie_name)
        href = str(target_a['href'])

        return movie_name, href
          
    def get_image_url(self):
        _, href = self.get_random_name_href('acao', 'netflix')
        
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(href, headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        img_tag = soup.find('img', class_='film__cartaz__img center-block img-responsive lazy-inline-image')

        src = str(img_tag['data-src'])
        return src

    def copy_paste_image(self):
        src = self.get_image_url()
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
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "div[class*='g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o r7fjleex bs7a17vp ov67bkzj'] p[class*='copyable-text']")))

        text_box_on_img = self.browser.find_element(By.CSS_SELECTOR, "div[class*='g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o r7fjleex bs7a17vp ov67bkzj'] p[class*='copyable-text']")
        text_box_on_img.click()
    
        message = 'Teste'
        lines = message.split("\n")
        for line in lines:
            text_box_on_img.send_keys(line)
            text_box_on_img.send_keys(Keys.SHIFT, Keys.ENTER)
        
        send_button = self.browser.find_element(By.CSS_SELECTOR, "div[class*='g0rxnol2 thghmljt p357zi0d rjo8vgbg ggj6brxn f8m0rgwh gfz4du6o r7fjleex bs7a17vp ov67bkzj'] div[aria-label='Enviar']")
        send_button.click()
        sleep(3)
    
    def get_description(self):
        ...

    