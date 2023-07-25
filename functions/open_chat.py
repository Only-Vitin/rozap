import functions
# Libraries
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

def open_chat(browser):
    while True:
        try:
            name_chat = input("Insira o nome do chat: ")

            chat = browser.find_element(By.XPATH, f"//span[@title='{name_chat}']")
            chat.click()
            sleep(2)

            initial_message = 'Opaa! Eu sou o RoZAP.\nEnvie */help* para ver os comandos'
            functions.send(browser, initial_message)
            break
        except NoSuchElementException:
            print("Digite um nome válido e que esteja aparecendo na tela")
            continue

def change_chat(browser, name_chat):
    while True:
        try:
            chat = browser.find_element(By.XPATH, f"//span[@title='{name_chat}']")
            chat.click()
            sleep(2)

            initial_message = 'Opaa! Eu sou o RoZAP.\nEnvie */help* para ver os comandos'
            functions.send(browser, initial_message)
            break
        except NoSuchElementException:
            print("Digite um nome válido e que esteja aparecendo na tela")
            continue