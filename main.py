import functions
# Libraries
import redis
from time import sleep
from unidecode import unidecode
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

REDIS_HOST = 'redis-18629.c308.sa-east-1-1.ec2.cloud.redislabs.com'
REDIS_PORT = 18629
REDIS_PASSWORD = '6DxAeE5KzFNff7h7QbwLUg9wKnnixi1E'
r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD, decode_responses=True)

def process_messages(browser):
    #Last Message
    last_author = None
    last_message = None
    while True:
        messages = browser.find_elements(By.CSS_SELECTOR, ".message-in, .message-out")

        for message in reversed(messages):
            message_class = message.get_attribute("class")
            if message_class.startswith("message-in"):
                WebDriverWait(browser, 10).until(EC.visibility_of(message))
                try:
                    last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
                    last_author = message.find_element(By.CSS_SELECTOR, "span[data-testid='author']").text
                    break
                except NoSuchElementException:
                    continue
            elif message_class.startswith("message-out"):
                WebDriverWait(browser, 10).until(EC.visibility_of(message))
                try:
                    last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
                    last_author = 'RoZAP'
                    break
                except NoSuchElementException:
                    continue

        last_message_text = last_message.text if last_message else ""
        if last_message_text:
            print("Última mensagem enviada por:", last_author)
            print("Última mensagem:", last_message_text)

        text = last_message_text.split(" ")
        
        #Functions
        if text[0] == '/changechat':
            if last_author == 'Eu':
                name_chat = text[1:]
                name_chat = ' '.join(name_chat)
                functions.change_chat(browser, name_chat)
            else:
                functions.send(browser, '*Ow fiii*, vc n pode usar esse comando não!')

        if text[0] == '/stop':
            if last_author == 'Eu':
                browser.quit()
                break
            else:
                functions.send(browser, '*Ow fiii*, vc n pode usar esse comando não!')
        
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
        
        keys = r.keys('*')
        if text[0] == '/list':
            lists = []
            if len(text) < 2:
                for key in keys:
                    key = key.split(' ')
                    if last_author in key:
                        key.pop()
                        key = ' '.join(key)
                        lists.append(key + '\n')
                        print(key)
                if len(lists) < 1:
                    functions.send(browser, 'Você não tem nenhuma lista')
                    continue
                else:
                    functions.send_withou_enter(browser, f'*Suas listas:*\n\n')
                    for listy in lists:
                        functions.send_withou_enter(browser, listy)
                    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
                    text_box.send_keys(Keys.ENTER)
            else:
                chave = f'{text[1]} {last_author}'
                if chave in keys:
                    element = r.get(chave)
                    functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                    functions.send(browser, element)
                else:
                    r.set(chave, '\n')
                    functions.send(browser, '*Dei uma criada na lista*')
        
        if text[0] == '/listadd':
            if len(text) < 2:
                functions.send(browser, '*Fiii*, escreve certo')
                continue
            else:
                item = ' '.join(text[2:])
                chave = f'{text[1]} {last_author}'
                if chave in keys:
                    r.append(chave, f'○ {item}\n')
                    element = r.get(chave)
                    functions.send(browser, 'Item adicionado com sucesso')
                    functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                    functions.send(browser, element)
                else:
                    functions.send(browser, 'Acho que essa lista não existe...')
                    continue
            
        if text[0] == '/listcut':
            if len(text) < 2:
                functions.send(browser, '*Fiii*, escreve certo')
                continue
            else:
                join_item = ' '.join(text[2:])
                item = f'○ {join_item}'
                chave = f'{text[1]} {last_author}'
                if chave in keys:
                    valor_atual = r.get(chave)
                    if valor_atual:
                        lista_valores = valor_atual.split('\n')
                        print(lista_valores)
                        if item in lista_valores:
                            lista_valores.remove(item)
                            novo_valor = '\n'.join(lista_valores)
                            r.set(chave, ' ')
                            r.append(chave, novo_valor)
                            
                            functions.send(browser, '*Item removido com sucesso*')
                            element = r.get(chave)
                            functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                            functions.send(browser, element)
                        else:
                            item = f'● ~{itemj}~'
                            if item in lista_valores:
                                lista_valores.remove(item)
                                novo_valor = '\n'.join(lista_valores)
                                r.set(chave, ' ')
                                r.append(chave, novo_valor)
                                
                                functions.send(browser, '*Item removido com sucesso*')
                                element = r.get(chave)
                                functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                                functions.send(browser, element)
                            else:
                                functions.send(browser, '*O item especificado não existe na lista*')
                    else:
                        functions.send(browser, '*A chave especificada não existe no Redis*')
                else:
                    functions.send(browser, 'Acho que essa lista não existe...')
        
        if text[0] == '/listcheck':
            if len(text) < 2:
                functions.send(browser, '*Fiii*, escreve certo')
                continue
            else:
                chave = f'{text[1]} {last_author}'
                itemj = ' '.join(text[2:])
                item = f'○ {itemj}'
                if chave in keys:
                    valor_atual = r.get(chave)
                    if valor_atual:
                        lista_valores = valor_atual.split('\n')
                        if item in lista_valores:
                            for i in range(len(lista_valores)):
                                if item == lista_valores[i]:
                                    lista_valores[i] = f'● ~{itemj}~'
                                    break
                            novo_valor = '\n'.join(lista_valores)
                            r.set(chave, ' ')
                            r.append(chave, novo_valor)
                            
                            functions.send(browser, '*Item checkado com sucesso*')
                            element = r.get(chave)
                            functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                            functions.send(browser, element)
                        else:
                            item = f'● ~{itemj}~'
                            if item in lista_valores:
                                for i in range(len(lista_valores)):
                                    if item == lista_valores[i]:
                                        lista_valores[i] = f'○ {itemj}'
                                        break
                                novo_valor = '\n'.join(lista_valores)
                                r.set(chave, ' ')
                                r.append(chave, novo_valor)
                                
                                functions.send(browser, '*Tirei o check*')
                                element = r.get(chave)
                                functions.send_withou_enter(browser, f'*Lista:* {text[1]}\n')
                                functions.send(browser, element)
                            else:
                                functions.send(browser, '*O item especificado não existe na lista*')
                    else:
                        functions.send(browser, '*A chave especificada não existe no Redis*')
                else:
                    functions.send(browser, 'Acho que essa lista não existe...')
        
        if text[0] == '/listdelete':
            if len(text) < 2:
                functions.send(browser, '*Fiii*, escreve certo')
                continue
            else:
                chave = f'{text[1]} {last_author}'
                if chave in keys:
                    r.delete(chave)
                    functions.send(browser, 'Lista deletada com sucesso')
                else:
                    functions.send(browser, 'Acho que essa lista não existe...')
        
        for i in range(len(text)):
            text[i] = text[i].lower()
        if 'rozap' in text:
            functions.send(browser, 'Qual foi irmão? Pq c ta falando meu nome em vão')
        sleep(1)

def main():
    browser = functions.configure_browser()
    functions.open_chat(browser)
    process_messages(browser)

if __name__ == '__main__':
    main()