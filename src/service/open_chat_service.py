from time import sleep
from selenium.webdriver.common.by import By


class ChatService():

    def __init__(self, browser):
        self.browser = browser
        self.chats = self.browser.find_elements(By.CSS_SELECTOR, "div[class='lhggkp7q ln8gz9je rx9719la']")

    def open_chat_on_archived(self):
        archived = self.browser.find_element(By.XPATH, '//div[text()="Arquivadas"]')
        archived.click()
        sleep(1)

    def click_on_chats(self, index):
        chat = self.chats[index]
        chat.click()
        sleep(0.5)