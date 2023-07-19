import functions
# Libraries
from time import sleep
from unidecode import unidecode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

def open_chat(browser):
    while True:
        try:
            name_chat = input("Insira o nome do chat: ")

            chat = browser.find_element(By.XPATH, f"//span[@title='{name_chat}']")
            chat.click()
            sleep(2)

            initial_message = 'Opaa! Eu sou o RoZAP\nEnvie */help* para ver os comandos'
            functions.send(browser, initial_message)
            break
        except NoSuchElementException:
            print("Digite um nome válido e que esteja aparecendo na tela")
            continue

def process_messages(browser):
    #Last Message
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
        
    #Functions
        if text[0] == '/changechat':
            open_chat(browser)

        if text[0] == '/help':
            help_message = '*Comandos:*\n\n*/phrase (nome do autor)* - Envia uma frase aleatória do autor desejado\n*/language (idioma)* - Mostra o código dos idiomas\n*/translate (código do idioma do texto) (código do idioma desejado) (texto)* - Traduz um texto para o idioma selecionado\n*/lyrics (nome da música)* - Envia a letra da música\n\n*Obs:* não precisa dos parênteses'
            functions.send(browser, help_message)

        if text[0] == '/phrase':
            try:
                if len(text) < 3:
                    if len(text) < 2:
                        error_message = 'Digita o comando certo ai vey...'
                        functions.send(browser, error_message)
                        continue
                    author = text[1]
                else:
                    text.pop(0)
                    author = '_'.join(text)

                author = unidecode(author.lower())
                phrase, author_name = functions.get_phrase(author)
                print("Frase:", phrase)

                if len(phrase) < 450:
                    functions.send(browser, f'*{author_name}:*\n\n{phrase}')
                else:
                    error_message = '*Ops!* Acho que a frase é muito grande. Tente novamente, por favor.'
                    functions.send(browser, error_message)
                    continue
            except IndexError:
                error_message = 'Foi mal ;-; Não consegui encontrar esse autor. Tente com um diferente, por favor.'
                functions.send(browser, error_message)
                continue
        
        if text[0] == '/language':
            try:
                termo = unidecode(text[1].lower())
                resultado = functions.find_language(termo)
                if resultado:
                    functions.send_withou_enter(browser, '*Idiomas encontrados:* \n')
                    for _, codigo in resultado.items():
                        lan_message = f"{codigo}"
                        functions.send_withou_enter(browser, lan_message + '\n')
                    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                    text_box.send_keys(Keys.ENTER)
                else:
                    error_message = 'Não encontrei nenhum idioma com esse nome... tem certeza que escreveu certo?'
                    functions.send(browser, error_message)
            except IndexError:
                error_message = '*É...* acho que tu mandou errado.'
                functions.send(browser, error_message)
                continue
            
        if text[0] == '/translate':
            while True:
                try:
                    if len(text) < 4:
                        error_message = '*Ow...* acho que você digitou o comando erradamente.\nEnvie */help* para ver a sintaxe do comando'
                        message.send(browser, error_message)
                        continue
                    else:
                        language_r = text[1]
                        language_d = text[2]
                        text_to_translate = ' '.join(text[3:])
                        
                        language_r = unidecode(language_r)
                        language_d = unidecode(language_d)
                        print("Idioma do texto: ", language_r, "Idioma desejado: ", language_d)
                        
                        translated_text = functions.translate(browser, language_r, language_d, text_to_translate)
                        
                        functions.send(browser, f'*Texto Traduzido:*\n\n{translated_text}')
                        break
                except IndexError:
                    error_message = '*Hm...* Não consegui traduzir'
                    functions.send(browser, error_message)
                    continue
        
        if text[0] == '/lyrics':
            try:
                if len(text) < 2:
                    error_message = '*Fiii*, escreve certo'
                    functions.send(browser, error_message)
                    continue
                music = ' '.join(text[1:])
                lyrics, music_name = functions.get_lyrics(music)
                if lyrics:
                    wait_message = '*Aguarde um momento...*'
                    functions.send(browser, wait_message)
                    functions.send_withou_enter(browser, f'Letra da música *"{music_name}"*\n\n')
                    for phrases in lyrics:
                        functions.send_withou_enter(browser, phrases + "\n")
                    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                    text_box.send_keys(Keys.ENTER)
                else:
                    error_message = 'Rapazzz tá certo isso ??? Não achei a música'
                    functions.send(browser, error_message)
                    continue
            except AttributeError:
                error_message = '*Ent...* não achei a música, quer tentar de novo ?'
                functions.send(browser, error_message)
                continue
        
        for i in range(len(text)):
            text[i] = text[i].lower()
        if 'rozap' in text:
            rozap_message = 'Qual foi irmão? Pq c ta falando meu nome em vão'
            functions.send(browser, rozap_message)
        sleep(1)

def main():
    browser = functions.configure_browser()
    open_chat(browser)
    process_messages(browser)

if __name__ == '__main__':
    main()