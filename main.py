import requests
from time import sleep
from random import randint
from bs4 import BeautifulSoup
from unidecode import unidecode
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def configure_browser():
    profile_path = r'C:\Users\vitin\AppData\Roaming\Mozilla\Firefox\Profiles\mhhsjylt.default-release'
    options = FirefoxOptions()
    options.add_argument("--lang=pt")
    options.profile = profile_path

    service = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service, options=options)
    browser.get('https://web.whatsapp.com/')
    browser.set_window_size(1000, 700)

    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[0])

    return browser

def open_chat(browser):
    while True:
        try:
            name_chat = input("Insira o nome do chat: ")

            chat = browser.find_element(By.XPATH, f"//span[@title='{name_chat}']")
            chat.click()
            sleep(2)

            initial_message = 'Opaa! Eu sou o RoZAP\nEnvie */help* para ver os comandos'
            send_message(browser, initial_message)
            break
        except NoSuchElementException:
            print("Digite um nome válido e que esteja aparecendo na tela")
            continue

def send_message(browser, message):
    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
    for letter in message:
        text_box.send_keys(letter)
    text_box.send_keys(Keys.ENTER)

def get_phrase(author):
    page = requests.get(f'https://www.pensador.com/autor/{author}')
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
    
    atributes = {'class':'PZPZlf ssJ7i B5dxMb'}
    music_name = soup.find_all('span', attrs=atributes)
    
    return lyrics, music_name

def translate(browser, language_r, language_d, text):
    browser.switch_to.window(browser.window_handles[1])
    browser.get(f'https://translate.google.com.br/?hl=pt-BR&sl={language_r}&tl={language_d}&text={text}&op=translate')
    
    while True:
        try:
            translated = browser.find_element(By.CSS_SELECTOR, "div.lRu31")
            break
        except NoSuchElementException:
            continue
    
    translated_text = translated.text if translated else ""
    browser.switch_to.window(browser.window_handles[0])
    
    return translated_text

idiomas = {'africaner': 'Africâner: af', 'albanes': 'Albanês: sq', 'amarico': 'Amárico: am', 'arabe': 'Árabe: ar', 'armenio': 'Armênio: hy', 'azerbaijano': 'Azerbaijano: az', 'basco': 'Basco: eu', 'bielorrusso': 'Bielorrusso: be', 'bengali': 'Bengali: bn', 'bosnio': 'Bósnio: bs', 'bulgaro': 'Búlgaro: bg', 'catalao': 'Catalão: ca', 'cebuano': 'Cebuano: ceb', 'chines (simplificado)': 'Chinês (simplificado): zh-CN', 'chines (tradicional)': 'Chinês (tradicional): zh-TW', 'corsico': 'Córsico: co', 'croata': 'Croata: hr', 'tcheco': 'Tcheco: cs', 'dinamarques': 'Dinamarquês: da', 'holandes': 'Holandês: nl', 'ingles': 'Inglês: en', 'esperanto': 'Esperanto: eo', 'estoniano': 'Estoniano: et', 'finlandes': 'Finlandês: fi', 'frances': 'Francês: fr', 'frisio': 'Frísio: fy', 'galego': 'Galego: gl', 'georgiano': 'Georgiano: ka', 'alemao': 'Alemão: de', 'grego': 'Grego: el', 'guzerate': 'Guzerate: gu', 'crioulo haitiano': 'Crioulo haitiano: ht', 'hausa': 'Hauçá: ha', 'havaiano': 'Havaiano: haw', 'hebraico': 'Hebraico: he ou iw', 'hindi': 'Hindi: hi', 'hmong': 'Hmong: hmn', 'hungaro': 'Húngaro: hu', 'islandes': 'Islandês: is', 'igbo': 'Igbo: ig', 'indonesio': 'Indonésio: id', 'irlandes': 'Irlandês: ga', 'italiano': 'Italiano: it', 'japones': 'Japonês: ja', 'javanes': 'Javanês: jv', 'canara': 'Canará: kn', 'cazaque': 'Cazaque: kk', 'cmer': 'Cmer: km', 'kinyarwanda': 'Kinyarwanda: rw', 'coreano': 'Coreano: ko', 'curdo': 'Curdo: ku', 'quirguiz': 'Quirguiz: ky', 'laosiano': 'Laosiano: lo', 'latim': 'Latim: la', 'leton': 'Letão: lv', 'lituano': 'Lituano: lt', 'luxemburgues': 'Luxemburguês: lb', 'macedonio': 'Macedônio: mk', 'malgaxe': 'Malgaxe: mg', 'malaio': 'Malaio: ms', 'malaiala': 'Malaiala: ml', 'maltes': 'Maltês: mt', 'maori': 'Maori: mi', 'marata': 'Marata: mr', 'mongol': 'Mongol: mn', 'myanmar (birmanes)': 'Myanmar (birmanês): my', 'nepales': 'Nepalês: ne', 'noruegues': 'Norueguês: no', 'nianja (chichewa)': 'Nianja (Chichewa): ny', 'oria': 'Oriá: or', 'pashto': 'Pashto: ps', 'persa': 'Persa: fa', 'polones': 'Polonês: pl', 'portugues (portugal, brasil)': 'Português (Portugal, Brasil): pt', 'punjabi': 'Punjabi: pa', 'romeno': 'Romeno: ro', 'russo': 'Russo: ru', 'samoano': 'Samoano: sm', 'gaelico escoces': 'Gaélico escocês: gd', 'servio': 'Sérvio: sr', 'sesoto': 'Sesoto: st', 'xona': 'Xona: sn', 'sindi': 'Sindi: sd', 'sinhala (cingales)': 'Sinhala (cingalês): si', 'eslovaco': 'Eslovaco: sk', 'esloveno': 'Esloveno: sl', 'somali': 'Somali: so', 'espanhol': 'Espanhol: es', 'sundanes': 'Sundanês: su', 'suaili': 'Suaíli: sw', 'sueco': 'Sueco: sv', 'tagalo (filipino)': 'Tagalo (filipino): tl', 'tajique': 'Tajique: tg', 'tamil': 'Tâmil: ta', 'tartaro': 'Tártaro: tt', 'telugu': 'Telugu: te', 'tailandes': 'Tailandês: th', 'turco': 'Turco: tr', 'turcomano': 'Turcomano: tk', 'ucraniano': 'Ucraniano: uk', 'urdu': 'Urdu: ur', 'uyghur': 'Uyghur: ug', 'usbeque': 'Usbeque: uz', 'vietnamita': 'Vietnamita: vi', 'gales': 'Galês: cy', 'xosa': 'Xosa: xh', 'idiche': 'Ídiche: yi', 'ioruba': 'Iorubá: yo', 'zulu': 'Zulu: zu'}
def find_language(palavra):
    resultado = {}
    for idioma, codigo in idiomas.items():
        if palavra in idioma:
            resultado[idioma] = codigo
    return resultado

def process_messages(browser):
    while True:
        messages = browser.find_elements(By.CSS_SELECTOR, ".message-in, .message-out")
        last_message = None

        for message in reversed(messages):
            if message.get_attribute("class").startswith("message-in"):
                WebDriverWait(browser, 10).until(EC.visibility_of(message))
                try:
                    last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
                    break
                except NoSuchElementException:
                    continue
            elif message.get_attribute("class").startswith("message-out"):
                WebDriverWait(browser, 10).until(EC.visibility_of(message))
                try:
                    last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
                    break
                except NoSuchElementException:
                    continue

        last_message_text = last_message.text if last_message else ""
        if last_message_text:
            print("Última mensagem enviada:", last_message_text)

        text = last_message_text.split(" ")

        if text[0] == '/changechat':
            open_chat(browser)

        if text[0] == '/help':
            help_message = '*Comandos:*\n\n*/phrase (nome do autor)* - Envia uma frase aleatória do autor desejado\n*/translate (código do idioma do texto) (código do idioma desejado) (texto)* - Traduz um texto para o idioma selecionado\n*/language (idioma)* - Mostra o código dos idiomas\n\n*Obs:* não precisa dos parênteses'
            send_message(browser, help_message)

        if text[0] == '/phrase':
            try:
                if len(text) < 3:
                    author = text[1]
                else:
                    text.pop(0)
                    author = '_'.join(text)

                author = unidecode(author.lower())
                phrase, author_name = get_phrase(author)
                print("Frase:", phrase)

                if len(phrase) < 450:
                    send_message(browser, f'*{author_name}:*\n\n{phrase}')
                else:
                    error_message = '*Ops!* Acho que a frase é muito grande. Tente novamente, por favor.'
                    send_message(browser, error_message)
                    continue
            except IndexError:
                error_message = 'Foi mal ;-; Não consegui encontrar esse autor. Tente com um diferente, por favor.'
                send_message(browser, error_message)
                continue
        
        if text[0] == '/language':
            try:
                termo = unidecode(text[1].lower())
                resultado = find_language(termo)
                if resultado:
                    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                    for letter in '*Idiomas encontrados:* ':
                        text_box.send_keys(letter)
                    text_box.send_keys(Keys.SHIFT + Keys.ENTER)
                    
                    for idioma, codigo in resultado.items():
                        lan_message = f"{codigo}"
                        text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                        for letter in lan_message:
                            text_box.send_keys(letter)
                        text_box.send_keys(Keys.SHIFT + Keys.ENTER)
                    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                    text_box.send_keys(Keys.ENTER)
                else:
                    error_message = 'Não encontrei nenhum idioma com esse nome... tem certeza que escreveu certo?'
                    send_message(browser, error_message)
            except IndexError:
                error_message = '*É...* acho que tu mandou errado.'
                send_message(browser, error_message)
                continue
            
        if text[0] == '/translate':
            while True:
                try:
                    if len(text) < 4:
                        error_message = '*Ow...* acho que você digitou o comando erradamente.\nEnvie */help* para ver a sintaxe do comando'
                        send_message(browser, error_message)
                        continue
                    else:
                        language_r = text[1]
                        language_d = text[2]
                        text_to_translate = ' '.join(text[3:])
                        
                        language_r = unidecode(language_r)
                        language_d = unidecode(language_d)
                        print("Idioma do texto: ", language_r, "Idioma desejado: ", language_d)
                        
                        translated_text = translate(browser, language_r, language_d, text_to_translate)
                        
                        send_message(browser, f'*Texto Traduzido:*\n\n{translated_text}')
                        break
                except IndexError:
                    error_message = '*Hm...* Não consegui traduzir'
                    send_message(browser, error_message)
                    continue
        
        if text[0] == '/lyrics':
            text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
            music = ' '.join(text[1:])
            lyrics, music_name = get_lyrics(music)
            if lyrics:
                send_message(browser, f'*Letra da música "{music_name}":*\n\n')
                for phrases in lyrics:
                    send_message(browser, phrases)
                    text_box.send_keys(Keys.SHIFT + Keys.ENTER)
                text_box.send_keys(Keys.ENTER)
            else:
                error_message = 'Rapazzz tá certo isso ??? Não achei a música'
                send_message(browser, error_message)
                continue
        
        for i in range(len(text)):
            text[i] = text[i].lower()
        if 'rozap' in text:
            rozap_message = 'Qual foi irmão? Pq c ta falando meu nome em vão'
            send_message(browser, rozap_message)
        sleep(1)

def main():
    browser = configure_browser()
    input("Faça a autenticação no WhatsApp Web e pressione Enter para continuar...")
    sleep(1)
    open_chat(browser)
    process_messages(browser)

if __name__ == '__main__':
    main()