from service import Stop, Help, Phrases
from utils import send_message


def verify_commands(browser, text, last_author):
    if text[0] == '/stop':
        op_stop = Stop(browser, last_author)
        op_stop.stop_program()

    elif text[0] == '/help':
        op_help = Help(browser)
        op_help.show_help_message()

    elif text[0] == '/helplist':
        op_help = Help(browser)
        op_help.show_help_list_message()

    elif text[0] == '/phrase':
        op_phrases = Phrases(browser, text)
        op_phrases.show_phrase()

    elif text[0] == '/language':
        ...

    elif text[0] == '/translate':
        ...

    elif text[0] == '/lyrics':
        ...

    elif text[0] == '/list':
        ...

    elif text[0] == '/listadd':
        ...

    elif text[0] == '/listcut':
        ...

    elif text[0] == '/listcheck':
        ...

    elif text[0] == '/listdelete':
        ...

    for i in range(len(text)):
        text[i] = text[i].lower()
    if 'rozap' in text:
        send_message(browser, 'Qual foi irmão? Pq c ta falando meu nome em vão')
