import bs4
import requests
import pprint

MAP_KEY = "AIzaSyA63EmB7d3J1w_6axs28keyc0tVaxhsnIA"
keywords = "openclassrooms+adresse"

r = requests.get(('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}').format(keywords, MAP_KEY))
file = r.json()
adress_answer = file['results'][0]['formatted_address']
lat_answer = file['results'][0]['geometry']['location']['lat']
lng_answer = file['results'][0]['geometry']['location']['lng']
for element in file['results']:
    pprint.pprint(element)