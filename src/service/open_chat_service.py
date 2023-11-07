from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

class ChatService():

    def __init__(self, browser):
        self.browser = browser
        self.chats = self.browser.find_elements(By.CSS_SELECTOR, "div[class='gfz4du6o r7fjleex'] div[class='lhggkp7q ln8gz9je rx9719la']")

    def open_chat_on_archived(self):
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, ".selectable-text")))
        while True:
            try:
                archived = self.browser.find_element(By.XPATH, '//div[text()="Arquivadas"]')
                archived.click()
                break
            except NoSuchElementException:
                continue

    def click_on_chats(self, index):
        try:
            chat = self.chats[index]
            notification_span = chat.find_element(By.CSS_SELECTOR, 'span[aria-label="Não lidas"]')
            chat.click()
        except NoSuchElementException:
            ...