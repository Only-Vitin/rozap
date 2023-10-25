from selenium.common.exceptions import NoSuchElementException

from service import ChatService
from utils import send_message


def open_chat(browser):
    while True:
        try:
            name_chat = input("Insira o nome do chat: ")
            
            chat_service = ChatService(browser)
            chat_service.open_chat_on_archived(name_chat)

            initial_message = 'Opaaa, bãozin fi? Eu sou o RoZAP.\nManda um */help* para ver os comandos'
            send_message(browser, initial_message)
            break
        except NoSuchElementException:
            print("Digite um nome válido e que esteja aparecendo na tela")
            continue
