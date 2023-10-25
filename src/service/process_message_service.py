from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


class ProcessMessageService():

    def __init__(self, browser):
        self.browser = browser

    def get_last_data_by_class(self, message_class, message):
        if message_class.startswith("message-in"):
            WebDriverWait(self.browser, 10).until(EC.visibility_of(message))

            last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
            author_div = message.find_element(By.CSS_SELECTOR, "div[class*='copyable-text']")
            last_author_data = author_div.get_attribute("data-pre-plain-text")
            last_author = last_author_data.split()
            last_author = last_author[-1].replace(":", "")
        elif message_class.startswith("message-out"):
            WebDriverWait(self.browser, 10).until(EC.visibility_of(message))
            
            last_message = message.find_element(By.CSS_SELECTOR, ".selectable-text")
            last_author = 'RoZAP'
        
        return last_message, last_author
    
    def get_last_message_author(self):
        while True:
            try:
                messages = self.browser.find_elements(By.CSS_SELECTOR, ".message-in, .message-out")

                for message in reversed(messages):
                    message_class = message.get_attribute("class")
                    last_message, last_author = self.get_last_data_by_class(message_class, message)
                    break

                last_message_text = last_message.text if last_message else ""
                text = last_message_text.split()
                
                return text, last_author
            except StaleElementReferenceException:
                continue
            except NoSuchElementException:
                continue