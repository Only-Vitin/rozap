from utils import send_message
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Help():

    def __init__(self, browser):
        self.browser = browser

    def show_help_message(self):
        send_message(self.browser, '*Comandos:*\n\n*/phrase (nome do autor)* - Envia uma frase aleatória do autor desejado\n*/language (idioma)* - Mostra o código dos idiomas\n*/translate (código do idioma do texto) (código do idioma desejado) (texto)* - Traduz um texto para o idioma selecionado\n*/lyrics (nome da música)* - Envia a letra da música\n*/helplist* - Comandos da lista\n\n*Obs:* não precisa dos parênteses')

        text_box = self.browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
        text_box.send_keys(Keys.ENTER)

    def show_help_list_message(self):
        send_message(self.browser, '*Comandos /list:*\n\n*/list* - Mostra as suas listas\n*/list (nome da lista)* - Mostra a lista selecionada\n*/list (nome da lista)* - Cria uma lista caso ainda não tenha uma lista com esse nome\n*/listadd (nome da lista) (item)* - Adiciona um item à lista\n*/listcut (nome da lista) (item)* - Remove o item selecionado\n*/listcheck (nome da lista) (item)* - Risca o item\n*/listdelete (nome da lista)* - Deleta a lista selecionada')
        
        text_box = self.browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
        text_box.send_keys(Keys.ENTER)