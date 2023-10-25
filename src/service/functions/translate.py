from unidecode import unidecode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

from storage_files import languages
from utils import send_message, send_message_without_enter


class Translate():
    
    def __init__(self, browser, text):
        self.browser = browser
        self.text = text
    
    def find_language(self, word):
        result = {}
        for language, code in languages.items():
            if word in language:
                result[language] = code
        return result
    
    def show_language_codes(self):
        try:
            term = unidecode(self.text[1].lower())
            result = self.find_language(term)
            if result:
                send_message_without_enter(self.browser, '*Idiomas encontrados:* \n')
                for _, codigo in result.items():
                    send_message_without_enter(self.browser, f'{codigo}\n')
                text_box = self.browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
                text_box.send_keys(Keys.ENTER)
            else:
                send_message(self.browser, 'Não encontrei nenhum idioma com esse nome... tem certeza que escreveu certo?')
        except IndexError:
            send_message(self.browser, 'É... acho que tu mandou errado.')
            
    def translate(self, browser, language_r, language_d, text):
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
    
    def show_translated_text(self):
        try:
            if len(self.text) < 4:
                send_message(self.browser, 'Ow... acho que você digitou o comando erradamente.')
            else:
                language_r = self.text[1]
                language_d = self.text[2]
                text_to_translate = ' '.join(self.text[3:])
                
                language_r = unidecode(language_r)
                language_d = unidecode(language_d)
                print("Idioma do texto: ", language_r, "Idioma desejado: ", language_d)
                
                translated_text = self.translate(self.browser, language_r, language_d, text_to_translate)
                
                send_message(self.browser, f'*Texto Traduzido:*\n\n{translated_text}')
        except IndexError:
            send_message(self.browser, 'Hm... Não consegui traduzir, mas juro que não foi culpa minha.')
            