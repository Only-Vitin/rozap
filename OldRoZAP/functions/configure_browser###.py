from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

def configure_browser():
    profile_path = r'C:\Users\vitin\AppData\Roaming\Mozilla\Firefox\Profiles\mhhsjylt.default-release'
    options = FirefoxOptions()
    options.add_argument("--lang=pt")
    options.profile = profile_path

    service = Service(GeckoDriverManager().install())
    browser = webdriver.Firefox(service=service, options=options)
    browser.get('https://web.whatsapp.com/')
    browser.set_window_size(1000, 700)

    browser.execute_script("window.open()")
    browser.switch_to.window(browser.window_handles[1])
    browser.switch_to.window(browser.window_handles[0])
    
    return browser