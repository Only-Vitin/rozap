import requests
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import send_message, send_message_without_enter


class Lyrics():
    def __init__(self, browser, text):
        self.browser = browser
        self.text = text
        
    def get_lyrics(self, music):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(f'https://www.google.com/search?q=letra+da+musica+{music}', headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        atributes = {'jsname':'U8S5sf'}
        stanzas = soup.find_all('div', attrs=atributes)
        
        full_lyrics = []
        for i in stanzas:
            lyrics = []
            for line in i:
                line = line.get_text()
                lyrics.append(line)
            lyrics_str = "\n".join(lyrics).replace("\n\n", "\n") + "\n"
            full_lyrics.append(lyrics_str)
            
        atributes = {'data-attrid':'title'}
        music_name = soup.find('div', attrs=atributes).get_text()
        
        return full_lyrics, music_name
        
    def show_lyrics(self):
        try:
            if len(self.text) < 2:
                send_message(self.browser, 'Se pá que o comando ta errado hein.')
                return False
                
            music = ' '.join(self.text[1:])
            lyrics, music_name = self.get_lyrics(music)
            
            if lyrics:
                text_box = self.browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
                send_message(self.browser, '*Um minutinho...* ninguém é perfeito.')
                send_message_without_enter(self.browser, f'Letra da música *"{music_name}"*\n\n')
                for stanzas in lyrics:
                    send_message_without_enter(self.browser, stanzas)
                text_box.send_keys(Keys.ENTER)
            else:
                send_message(self.browser, 'Vey, não achei essa música ai não.')
        except AttributeError:
            send_message(self.browser, 'Ent... não achei essa música ai não, quer tentar de novo ?')
