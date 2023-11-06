from utils import send_message
from storage_files import genres_name, streamings_name


class HelpSuggest():

    def __init__(self, browser):
        self.browser = browser

    def show_help_suggest(self):
        genres_name_join = ', '.join(genres_name)
        streamings_name_join = ', '.join(streamings_name)
        send_message(self.browser, f"*Provedores disponíveis:* {streamings_name_join}\n\n*Gêneros disponíveis:* {genres_name_join}")