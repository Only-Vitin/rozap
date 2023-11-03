from service import Stop, Help, Phrases, Translate, Lyrics, Dict, Suggest
from utils import send_message


def verify_commands(browser, text, last_author):
    match text[0]:
        case '/stop':
            op_stop = Stop(browser, last_author)
            op_stop.stop_program()
            
        case '/help':
            op_help = Help(browser)
            op_help.show_help_message()

        case '/phrase':
            op_phrases = Phrases(browser, text)
            op_phrases.show_phrase()

        case '/language':
            op_language = Translate(browser, text)
            op_language.show_language_codes()

        case '/translate':
            op_translate = Translate(browser, text)
            op_translate.show_translated_text()
            
        case '/lyrics':
            op_lyrics = Lyrics(browser, text)
            op_lyrics.show_lyrics()

        case '/dict':
            op_dict = Dict(browser, text)
            op_dict.show_word_meaning()

        case '/suggest':
            op_suggest = Suggest(browser, text)
            op_suggest.open_movie()

    for i in range(len(text)):
        text[i] = text[i].lower()
    if 'rozap' in text:
        send_message(browser, f'O {last_author}... quem você pensa que é?')
