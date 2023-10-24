from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class ChatService():

    def __init__(self, browser):
        self.browser = browser

    def open_chat_on_archived(self, name_chat):
        archived = self.browser.find_element(By.XPATH, '//div[text()="Arquivadas"]')
        archived.click()
        sleep(1)

        chat = self.browser.find_element(By.CSS_SELECTOR, f"span[title='{name_chat}']")
        chat.click()
        sleep(2)
