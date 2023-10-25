import requests
from bs4 import BeautifulSoup
from unidecode import unidecode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils import send_message, send_message_without_enter


class Dict():

    def __init__(self, browser, text):
        self.browser = browser
        self.text = text

    def get_meaning(self, word):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(f'https://www.dicio.com.br/{word}/', headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        atributes = {'itemprop':'description'}
        stanzas = soup.find_all('p', attrs=atributes)
        
        full_meaning = []
        for i in stanzas:
            meanings = []
            for line in i:
                line = line.get_text()
                line = line + "\n"
                meanings.append(line)
            lyrics_str = "\n".join(meanings).replace("\n \n", "\n")
            lyrics_str = lyrics_str.replace("\n\n\n", "\n")
            full_meaning.append(lyrics_str)
            
        atributes = {'class':'tit-significado'}
        title = soup.find('h2', attrs=atributes).get_text()
        
        return full_meaning, title

    def show_word_meaning(self):
        try:
            if len(self.text) < 2:
                send_message(self.browser, 'Você entendeu como o comando funciona?')
            else:
                word = '-'.join(self.text[1:])
                word = unidecode(word.lower())
                meaning, title = self.get_meaning(word)

                if meaning:
                    send_message_without_enter(self.browser, f'*{title}*\n')
                    for stanzas in meaning:
                        send_message(self.browser, stanzas)
                else:
                    send_message(self.browser, 'Não achei essa palavra, e a culpa e do desenvolvedor né')
        except AttributeError:
            send_message(self.browser, 'Não encontrei essa palavra no site...')