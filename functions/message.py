from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def send(browser, message):
    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
    for letter in message:
        text_box.send_keys(letter)
    text_box.send_keys(Keys.ENTER)
    
def send_withou_enter(browser, message):
    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Mensagem"]')
    for letter in message:
        text_box.send_keys(letter)