#coding: utf-8
import wikipedia
import bs4
import requests
import pprint
from config import *

class Answer:

    def __init__(self):
        self.text_question = str()
        self.wordslist = []
        self.keywords = []
        self.url_answer = str()
        self.summary_answer = str()
        self.keywords_map = str()
        self.adress_answer = str()
        self.lat_answer = float()
        self.lng_answer = float()

    def create_wordslist(self):
        for element in TAB_LIST:
            self.text_question = self.text_question.replace(element," ")
        self.wordslist = self.text_question.split()

    def create_keywords(self,):
        word_to_delete=[]
        for word in self.wordslist:
            if word.lower() in STOP_WORDS_LIST:
                word_to_delete.append(word)
        for element in word_to_delete:
            self.wordslist.remove(element)
        self.keywords = self.wordslist[:]

    def wiki_answer(self):
        wiki_request = " ".join(self.keywords)
        wikipedia.set_lang("fr")
        answer = wikipedia.search(wiki_request)
        ans_page = wikipedia.page(answer[0])
        self.url_answer = ans_page.url
        self.summary_answer = wikipedia.summary(answer[0])

    def wiki_parsing(self):
        self.create_wordslist()
        self.create_keywords()
        self.wiki_answer()


    def google_map_request (self):
        r = requests.get(
            ('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}')
            .format(self.keywords_map, MAP_KEY))
        file = r.json()
        #for element in file['results']:
            #pprint.pprint(element)
        self.adress_answer = file['results'][0]['formatted_address']
        self.lat_answer = file['results'][0]['geometry']['location']['lat']
        self.lng_answer = file['results'][0]['geometry']['location']['lng']

    def creating_map_infos(self):
        self.keywords_map = "+".join(self.keywords).lower()
        self.google_map_request ()

if __name__ == "__main__":
    a = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms à Paris?"
    b = Answer()
    b.text_question = a
    b.wiki_parsing()
    b.creating_map_infos()
    pprint.pprint(b.__dict__)