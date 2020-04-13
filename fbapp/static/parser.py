# coding: utf-8
"""[Rules the class Answer]
"""
import wikipedia
import requests
from config import KEYS


class Answer:
    """Class 'parser.Answer' rule the datas send and collected
    from GoogleMap's and Wikipedia's APIs.
    and Actions.py files.

    Attributs (= Default):
    self.text_question = str()
    self.keywords_wiki = []
    self.keywords = []
    self.url_answer = str()
    self.summary_answer = str()
    self.keywords_map = str()
    self.adress_answer = str()
    self.lat_answer = float()
    self.lng_answer = float()

    Class methods:
        -_create_keywords
        -_wiki_answer
        -wiki_parsing
        -_google_map_request
        -creating_map_infos

    Example:
        question = Answer()
    """
    def __init__(self):
        self.text_question = str()
        self.keywords_wiki = []
        self.keywords = []
        self.url_answer = str()
        self.summary_answer = str()
        self.keywords_map = str()
        self.adress_answer = str()
        self.lat_answer = float()
        self.lng_answer = float()

    def _create_keywords(self, text_question):
        """Create a key words list of 'str' from a 'str' element
        in removing signs, numbers and useless words.

        Args:
        self {parser.Answer} -- [Use specificaly self.keywords attribut]
        text_question {STR} -- [Use to be a sentence with a least
        one usefull identifiable word]

        Return:
        No return.
        Modify self.keywords attribut.

        Example:
        self._create_keywords(text_question)

        """
        for element in KEYS['TAB_LIST']:
            text_question = text_question.replace(element, " ")
        wordslist = text_question.split()
        word_to_delete = []
        for word in wordslist:
            if word.lower() in KEYS['STOP_WORDS_LIST']:
                word_to_delete.append(word)
        for element in word_to_delete:
            wordslist.remove(element)
        self.keywords = wordslist[:]

    def _wiki_answer(self):
        """Create a specific key words list from self.keywords then
        use it for collecting datas from Wikipedia's API
        (sum up and wikipedia page url).

        Args:
        self {parser.Answer} -- [Use specificaly self.url_answer
        and self.summary_answer attributs]

        Return:
        No return.
        Modify self.summary_answer and self.url_answer attributs.

        Example:
        self._wiki_answer()

        """
        wiki_request = " ".join(self.keywords)
        wikipedia.set_lang("fr")
        answer = wikipedia.search(wiki_request)
        ans_page = wikipedia.page(answer[0])
        self.url_answer = ans_page.url
        self.summary_answer = wikipedia.summary(answer[0])

    def wiki_parsing(self):
        """Modify self.keywords attribut in calling _create_keywords()
        function, then rule the _wiki_answer() function with it. It create
        the story part of Papy bot answer.

        Args:
        self {parser.Answer} -- [Use specificaly self.keywords attribut]

        Return:
        No return.
        Modify self.keywords attribut.

        Example:
        self.wiki_parsing()

        """

        self._create_keywords(self.adress_answer)
        self._wiki_answer()

    def _google_map_request(self):
        """Create a specific key words list from self.keywords then
        use it for collecting datas from GoogleMap's API
        (location and formatted adress).

        Args:
        self {parser.Answer} -- [Use specificaly self.adress_answer,
        self.lat_answer and self.lng_answer attributs]

        Return:
        No return.
        Modify self.adress_answer, self.lat_answer and
        self.lng_answer attributs.

        Example:
        self._google_map_request ()
        """
        requ = requests.get(
            ('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}')
            .format(self.keywords_map, KEYS['MAP_KEY']))
        file = requ.json()
        for element in file:
            print(element)
        self.adress_answer = file['results'][0]['formatted_address']
        self.lat_answer = file['results'][0]['geometry']['location']['lat']
        self.lng_answer = file['results'][0]['geometry']['location']['lng']

    def creating_map_infos(self, text_question):
        """Modify self.keywords attribut from a text_question in
        calling _create_keywords() function, then rule the
        _google_map_request() function with it. It create
        the map and adress parts of Papy bot answer.

        Args:
        self {parser.Answer} -- [Use specificaly self.keywords attribut]

        Return:
        No return.
        Modify self.keywords attribut.

        Example:
        self.creating_map_infos(text_question)

        """
        self.text_question = text_question
        self._create_keywords(self.text_question)
        self.keywords_map = "+".join(self.keywords).lower()
        self._google_map_request()
