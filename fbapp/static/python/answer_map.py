# coding: utf-8
"""[Rules the class AnswerMap]
"""
import requests
from config import KEYS
from fbapp.static.python.answer import Answer


class AnswerMap(Answer):
    """Class 'answer_map.AnswerMap' rules string datas. It collects and
    cleans geographical informations about them from GoogleMap's API.

    Attributs (= Default):
    -self.keywords_map = str("")
    -self.adress_answer = str("")
    -self.lat_answer = float()
    -self.lng_answer = float()

    Class methods:
    -_google_map_request
    -creating_map_infos

    Example:
    question = AnswerMap()
    """
    def __init__(self):
        super().__init__()
        self.keywords_map = str()
        self.adress_answer = str()
        self.lat_answer = float()
        self.lng_answer = float()

    def google_map_request(self):
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
        map_request = requests.get(
            ('https://maps.googleapis.com/maps/api/place/' +
                ('textsearch/json?query={}&key={}').format(
                    self.keywords_map, KEYS['MAP_KEY']))
            )
        file = map_request.json()
        if file['results'] == []:
            self.adress_answer = "Aucune adresse de trouvée sur googlemap"
        else:
            self.adress_answer = file['results'][0]['formatted_address']
            self.lat_answer = file['results'][0]['geometry']['location']['lat']
            self.lng_answer = file['results'][0]['geometry']['location']['lng']
            self.success = True

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
        self.create_keywords(self.text_question)
        self.keywords_map = "+".join(self.keywords).lower()
        self.google_map_request()
