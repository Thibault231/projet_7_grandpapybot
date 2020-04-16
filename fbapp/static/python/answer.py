# coding: utf-8
"""[Rules the parent-class Answer]
"""
from config import KEYS


class Answer:
    """Class 'answer.Answer' rules string datas for creating
    a significant keywords list with them. It's a parent class
    for AnswerWiki and AnswerMap.

    Attributs (= Default):
    self.text_question = str()
    self.keywords = []

    Class methods:
        -_create_keywords
       
    Example:
        question = Answer()
    """
    def __init__(self):
        self.text_question = str()
        self.keywords = []
        self.success = False
        
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
