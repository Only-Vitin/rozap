from configure import ConfigureBrowser
from controller import ChatController


def main():
    config_browser = ConfigureBrowser()
    config_browser.open_windows()
    browser = config_browser.browser

    chat = ChatController(browser)
    chat.open_chat()


if __name__ == '__main__':
    main()
 