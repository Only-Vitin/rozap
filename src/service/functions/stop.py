from utils import send_message
from time import sleep


class Stop():

    def __init__(self, browser, last_author):
        self.browser = browser
        self.last_author = last_author

    def stop_program(self):
        if self.last_author == 'Eu':
            send_message(self.browser, 'Zzz Zzz Zzz')
            sleep(1)
            self.browser.quit()
        else:
            send_message(self.browser, f'Ó o cara, mó desumilde... eu sei onde você mora hein {self.last_author}')