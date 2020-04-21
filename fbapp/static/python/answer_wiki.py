# coding: utf-8
"""[Rules the class answer_wiki.AnswerWiki]
"""
import wikipedia
from fbapp.static.python.answer import Answer


class AnswerWiki(Answer):
    """Class 'answer_wiki.AnswerWiki' rules string datas. It collects and
    cleans informations about them from Wikipedia's API.

    Attributs (= Default):
    -self.wiki_request = []
    -self.url_answer = str()
    -self.summary_answer = str()

    Class methods:
    -_wiki_answer
    -wiki_parsing

    Example:
    question = AnswerWiki()
    """
    def __init__(self):
        super().__init__()
        self.wiki_request = []
        self.url_answer = str()
        self.summary_answer = str()

    def wiki_answer(self, keywords):
        """Create a specific key words list from self.keywords then
        use it for collecting datas from Wikipedia's API
        (sum up and wikipedia page url).

        Args:
        self {parser.Answer} -- [Use specificaly self.url_answer
        and self.summary_answer attributs]

        Return:
        No return.
        Modify self.wiki_request, self.summary_answer and
        self.url_answer attributs.

        Example:
        self._wiki_answer([keywords])

        """
        self.wiki_request = " ".join(keywords)
        wikipedia.set_lang("fr")
        answer = wikipedia.search(self.wiki_request)
        if answer == []:
            self.summary_answer = 'Rien de trouvé sur Wikipédia'
        else:
            ans_page = wikipedia.page(answer[0])
            self.url_answer = ans_page.url
            self.summary_answer = wikipedia.summary(answer[0])
            self.success = True
       
        return ans_page

    def wiki_parsing(self, text_question):
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
        self.create_keywords(text_question)
        self.wiki_answer(self.keywords)
