from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

    
def send_message(browser, message):
    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
    
    lines = message.split("\n")
    for line in lines:
        text_box.send_keys(line)
        text_box.send_keys(Keys.SHIFT, Keys.ENTER)
    text_box.send_keys(Keys.ENTER)
    
def send_message_without_enter(browser, message):
    text_box = browser.find_element(By.CSS_SELECTOR, 'div[title="Digite uma mensagem"]')
    
    lines = message.split("\n")
    for line in lines:
        text_box.send_keys(line)
        text_box.send_keys(Keys.SHIFT, Keys.ENTER)
        