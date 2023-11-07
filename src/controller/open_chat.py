from time import sleep
from service import ChatService


def open_chat(browser):
    chat_service = ChatService(browser)
    chat_service.open_chat_on_archived()
    sleep(1)

    return chat_service.chats

def click_chats(browser, index):
    chat_service = ChatService(browser)
    chat_service.click_on_chats(index)

def return_chats(browser):
    chat_service = ChatService(browser)
    
    return chat_service.chats
