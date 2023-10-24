from time import sleep
from service import ProcessMessageService


def read_messages(browser):
    process_message = ProcessMessageService(browser)
    text, last_author = process_message.get_last_message_author()
    print("Última mensagem enviada por:", last_author)
    print("Última mensagem:", text)

    sleep(0.5)
    return text, last_author
