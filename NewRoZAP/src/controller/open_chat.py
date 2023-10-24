from selenium.common.exceptions import NoSuchElementException

from service import ChatService
from utils import send_with_enter


class ChatController():
    def __init__(self, browser):
        self.browser = browser

    def open_chat(self):
        while True:
            try:
                name_chat = input("Insira o nome do chat: ")
                
                chat_service = ChatService(self.browser)
                chat_service.open_chat_on_archived(name_chat)

                initial_message = 'Opaa! Eu sou o RoZAP.\nEnvie */help* para ver os comandos'
                send_with_enter(self.browser, initial_message)
                break
            except NoSuchElementException:
                print("Digite um nome válido e que esteja aparecendo na tela")
                continue
