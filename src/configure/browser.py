import os
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class ConfigureBrowser():

    def __init__(self):
        self.options = ChromeOptions()
        self.service = Service(ChromeDriverManager().install())
        self.browser = self.configure_browser()

    def configure_browser(self):
        dir_path = os.getcwd()
        profile = os.path.join(dir_path, "profile", "wpp")
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument("--lang=pt")
        self.options.add_argument(r"user-data-dir={}".format(profile))
        
        browser = webdriver.Chrome(options=self.options, service=self.service)
        return browser

    def open_whatsapp_window(self):
        self.browser.get('https://web.whatsapp.com/')
        self.browser.set_window_size(1000, 700)
    
    def open_empty_window(self):
        self.browser.execute_script("window.open()")
        self.browser.execute_script("window.open()")
    
    def open_windows(self):
        self.open_empty_window()
        self.open_whatsapp_window()
        self.browser.switch_to.window(self.browser.window_handles[2])
        self.browser.switch_to.window(self.browser.window_handles[1])
        self.browser.switch_to.window(self.browser.window_handles[0])
        
