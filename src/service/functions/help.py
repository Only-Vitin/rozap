from utils import send_message


class Help():

    def __init__(self, browser):
        self.browser = browser

    def show_help_message(self):
        send_message(self.browser, '*Comandos:*\n\n*/phrase (nome do autor)* - Envia uma frase aleatória do autor desejado\n*/translate (código do idioma do texto) (código do idioma desejado) (texto)* - Traduz um texto para o idioma selecionado\n*/language (idioma)* - Mostra o código dos idiomas\n*/lyrics (nome da música)* - Envia a letra da música\n*/dict (palavra)* - Mostra o significado da palavra\n*/suggest (provedor) (filmes ou series) (gênero)* - Recomenda um filme/série\nObs: nenhum dos parâmetros são obrigatórios\n*/hsuggest* - Lista dos provedores e gêneros disponíveis no /suggest\n\n*Obs:* não precisa dos parênteses')
