import requests
from random import randint
from bs4 import BeautifulSoup

def get_phrase(author):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    page = requests.get(f'https://www.pensador.com/autor/{author}', headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    phrases = soup.find_all('p', class_='frase')
    nmr = randint(0, len(phrases))
    phrase = phrases[nmr].get_text()
    author_name = soup.find('span', class_='author-name').get_text()
    return phrase, author_name


def get_lyrics(music):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0'}
    page = requests.get(f'https://www.google.com/search?q=letra+da+musica+{music}', headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')
    atributes = {'jsname':'YS01Ge'}
    stanzas = soup.find_all('span', attrs=atributes)
    lyrics = []
    for i in stanzas:
        lyric = i.get_text()
        lyrics.append(lyric)
    atributes = {'data-attrid':'title'}
    music_name = soup.find('div', attrs=atributes).get_text()
    return lyrics, music_name