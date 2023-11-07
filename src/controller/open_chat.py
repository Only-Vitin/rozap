from time import sleep
from service import ChatService
from selenium.webdriver.common.by import By


def open_chat(browser):
    chat_service = ChatService(browser)
    chat_service.open_chat_on_archived()
    sleep(0.5)
    chats = browser.find_elements(By.CSS_SELECTOR, "div[class='gfz4du6o r7fjleex'] div[class='lhggkp7q ln8gz9je rx9719la']")
    first_chat = chats[-1]
    first_chat.click

    return chat_service.chats

def click_chats(browser, index):
    chat_service = ChatService(browser)
    chat_service.click_on_chats(index)

def return_chats(browser):
    chat_service = ChatService(browser)
    
    return chat_service.chats
