from configure import ConfigureBrowser
from controller import open_chat, read_messages, verify_commands


def main():
    config_browser = ConfigureBrowser()
    config_browser.open_windows()
    browser = config_browser.browser

    open_chat(browser)
    while True:
        text, last_author = read_messages(browser)
        verify_commands(browser, text, last_author)


if __name__ == '__main__':
    main()
