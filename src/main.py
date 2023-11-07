from configure import ConfigureBrowser
from controller import open_chat, read_messages, verify_commands, click_chats, return_chats

def main():
    config_browser = ConfigureBrowser()
    config_browser.open_windows()
    browser = config_browser.browser

    open_chat(browser)
    while True:
        chats = return_chats(browser)
        for index in range(len(chats)):
            click_chats(browser, index)
            text, last_author = read_messages(browser)
            if text and last_author:
                verify_commands(browser, text, last_author)

if __name__ == '__main__':
    main()
