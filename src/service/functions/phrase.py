from unidecode import unidecode
import requests
from random import randint
from bs4 import BeautifulSoup
from utils import send_message


class Phrases():

    def __init__(self, browser, text):
        self.browser = browser
        self.text = text

    def get_phrase(self, author):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'}
        page = requests.get(f'https://www.pensador.com/autor/{author}', headers=headers)
        soup = BeautifulSoup(page.text, 'html.parser')

        phrases = soup.find_all('p', class_='frase')
        nmr = randint(0, len(phrases))

        phrase = phrases[nmr].get_text()
        author_name = soup.find('span', class_='author-name').get_text()
        return phrase, author_name

    def show_phrase(self):
        try:
            if len(self.text) < 3:
                if len(self.text) < 2:
                    send_message(self.browser, 'Digita o comando certo ai vey...')
                    return False
                author = self.text[1]
            else:
                self.text.pop(0)
                author = '_'.join(self.text)

            author = unidecode(author.lower())
            phrase, author_name = self.get_phrase(author)
            print("Frase:", phrase)

            if len(phrase) < 450:
                send_message(self.browser, f'*{author_name}:*\n\n{phrase}')
            else:
                send_message(self.browser, 'Acho que a frase é muito grande >~< Tenta de novo ai por favor.')
        except IndexError:
            send_message(self.browser, 'Foi mal ;-; Não achei esse autor. Tenta com um diferente, por favor.')
