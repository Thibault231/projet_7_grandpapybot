#coding: utf-8
import wikipedia
import bs4
import requests
import pprint

STOP_WORDS_LIST = ["a","abord","absolument","adresse","afin","ah","ai","aie","ailleurs","ainsi","ait",
"allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après",
"as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura",
"auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles",
"auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat",
"beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci",
"celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain",
"certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune",
"chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième",
"cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","connais","connait",
"concernant", "contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier",
"derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux",
"deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent",
"différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers",
"diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont",
"douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement",
"egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ",
"es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur",
"f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","grandpy","h","ha","hein",
"hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé",
"hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le",
"lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là",
"lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien",
"mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon",
"moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins",
"necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment",
"notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on",
"ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|",
"où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier",
"particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux",
"pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs",
"possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement",
"premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu",
"puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre",
"quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque",
"quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement",
"remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s",
"sa","sacrebleu","sait","salut","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble",
"semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si",
"sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous",
"souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit",
"suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac",
"tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien",
"tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois",
"toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u",
"un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt",
"vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres",
"w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"]

TAB_LIST = ["!","?",".","-",",","'","0","1","2","3","4","5","6","7","8","9"]

def create_wordslist(text_question):
    for element in TAB_LIST:
        text_question = text_question.replace(element," ")
    wordslist = text_question.split()
    return wordslist

def create_keywords(wordslist):
    word_to_delete=[]
    for word in wordslist:
        if word.lower() in STOP_WORDS_LIST:
            word_to_delete.append(word)
    for element in word_to_delete:
        wordslist.remove(element)
    keywords = wordslist
    return keywords

def wiki_answer(keywords):
    wiki_request = " ".join(keywords)
    wikipedia.set_lang("fr")
    answer = wikipedia.search(wiki_request)
    ans_page = wikipedia.page(answer[0])
    ans_url = ans_page.url
    ans_summary = wikipedia.summary(answer[0])
    return ans_url, ans_summary

def wiki_parsing(text_question):
    wordslist = create_wordslist(text_question)
    keywords = create_keywords(wordslist)
    print(keywords)
    url_answer, summary_answer = wiki_answer(keywords)
    return url_answer, summary_answer


def google_map_request (keywords_map, map_key):
    r = requests.get(('https://maps.googleapis.com/maps/api/place/textsearch/json?query={}&key={}').format(keywords_map, map_key))
    file = r.json()
    #for element in file['results']:
        #pprint.pprint(element)
    adress_answer = file['results'][0]['formatted_address']
    lat_answer = file['results'][0]['geometry']['location']['lat']
    lng_answer = file['results'][0]['geometry']['location']['lng']
    return adress_answer, lat_answer, lng_answer

def creating_map_infos(text_question, map_key):
    wordslist = create_wordslist(text_question)
    keywords = create_keywords(wordslist)
    keywords_map = "+".join(keywords).lower()
    adress_answer, lat_answer, lng_answer = google_map_request (keywords_map, map_key)
    return adress_answer, lat_answer, lng_answer

if __name__ == "__main__":
    a = "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?"
    b = "AIzaSyA63EmB7d3J1w_6axs28keyc0tVaxhsnIA"
    c = "openclassrooms+adresse"
    adress_answer, lat_answer, lng_answer = creating_map_infos(a, b)
    url_answer, summary_answer = wiki_parsing(adress_answer)
    print(url_answer, summary_answer)
