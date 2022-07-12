import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import warnings
from tkinter import *
import re
from datetime import datetime
from datetime import date

FONT_BOLD = "Helvetica 13 bold"

ceas = datetime.now()
current_time = ceas.strftime("%H:%M:%S")
azi = date.today()

warnings.filterwarnings('ignore')

#deschidere si prelucrare fisier
with open('bot.txt.txt', 'r') as file:
    data = file.read().replace('\n', '')

corpus = data

bancuri = ["Cum strigi un caine in biserica?\nMAICUUTU-le","Barbatul care nu are noroc la femei, nu stie ce noroc are",
           "Doua baloane zboara. Unul spune: Mai poti?\nCelalat: Mai poc!","Cu ce l-au luat jandarmii pe Newton de la sectie?"
           "\nCu forta!","Un stand-up s a ținut in chernobyl, pentru prima oară comediantul a văzut oameni râzând peste mustață",
           "Cum e împărțită inima roboților din transformers?\nÎn atrii și vehicule"]


alphabets= "([A-Za-z])"
prefixes = "(Mr|St|Mrs|Ms|Dr)[.]"
suffixes = "(Inc|Ltd|Jr|Sr|Co)"
starters = "(Mr|Mrs|Ms|Dr|He\s|She\s|It\s|They\s|Their\s|Our\s|We\s|But\s|However\s|That\s|This\s|Wherever)"
acronyms = "([A-Z][.][A-Z][.](?:[A-Z][.])?)"
websites = "[.](com|net|org|io|gov)"

#divizare in propozitii
def split_into_sentences(text):
    text = " " + text + "  "
    text = text.replace("\n"," ")
    text = re.sub(prefixes,"\\1<prd>",text)
    text = re.sub(websites,"<prd>\\1",text)
    if "Ph.D" in text: text = text.replace("Ph.D.","Ph<prd>D<prd>")
    text = re.sub("\s" + alphabets + "[.] "," \\1<prd> ",text)
    text = re.sub(acronyms+" "+starters,"\\1<stop> \\2",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>\\3<prd>",text)
    text = re.sub(alphabets + "[.]" + alphabets + "[.]","\\1<prd>\\2<prd>",text)
    text = re.sub(" "+suffixes+"[.] "+starters," \\1<stop> \\2",text)
    text = re.sub(" "+suffixes+"[.]"," \\1<prd>",text)
    text = re.sub(" " + alphabets + "[.]"," \\1<prd>",text)
    if "”" in text: text = text.replace(".”","”.")
    if "\"" in text: text = text.replace(".\"","\".")
    if "!" in text: text = text.replace("!\"","\"!")
    if "?" in text: text = text.replace("?\"","\"?")
    text = text.replace(".",".<stop>")
    text = text.replace("?","?<stop>")
    text = text.replace("!","!<stop>")
    text = text.replace("<prd>",".")
    sentences = text.split("<stop>")
    sentences = sentences[:-1]
    sentences = [s.strip() for s in sentences]
    return sentences

sentece_list = split_into_sentences(data)

# functiile de salutare/prelucrarea input utilizator
def greeting_response(text):
  text = text.lower()

  #Bots greeting response
  bot_greetings = ['Salutare', 'Buna', 'Buna ziua', 'Va salut cu respcect', 'Buna, studentule', 'Salut','Hei :)']
  #Users greeting
  user_greetings = ['salut', 'buna', 'ceau', 'buna ziua', 'hey', 'buna dimineata', 'salut!',
                    'buna!', 'ceau!', 'buna ziua!', 'hey!', 'buna dimineata!','salutare','salutare!']

  for word in text.split():
    if word in user_greetings:
      return random.choice(bot_greetings) + '!'

def index_sort(list_var):
  length = len(list_var)
  list_index = list(range(0, length))

  x = list_var
  for i in range(length):
   for j in range(length):
     if x[list_index[i]] > x[list_index[j]]:
       temp = list_index[i]
       list_index[i] = list_index[j]
       list_index[j] = temp

  return list_index

#crearea de raspunsuri
def bot_response(user_input):
 user_input = user_input.lower()
 sentece_list.append(user_input)
 bot_response = ''
 cm = CountVectorizer().fit_transform(sentece_list)
 similarity_scores = cosine_similarity(cm[-1], cm)
 similarity_scores_list = similarity_scores.flatten()
 index = index_sort(similarity_scores_list)
 index = index[1:]
 response_flag = 0
 ok = 0

 j = 0


 for i in range(len(index)):
   if similarity_scores_list[index[i]] > 0.2:
     bot_response = bot_response + ' ' + sentece_list[index[i]]
     response_flag = 1
     j = j + 1
   if j > 2:
      break

   if response_flag == 0:
    bot_response = random.choice(["Imi cer scuze, nu inteleg.", "Scuze, nu inteleg.", "Te rog adreseaza-mi alta intrebare!",
                                 "Nu te pot ajuta la aceasta intrebare."])


 sentece_list.remove(user_input)

 return bot_response

#Start chat


exit_list = ['iesire', 'la revedere', 'o zi buna in continuare', 'terminare','am terminat','multumesc de ajutor','exit'
             ,'stop','la revedere!','o zi buna!','o zi buna in continuare!','am terminat!','multumesc de ajutor!',
             'multumesc','multumesc!','va multumesc!','va multumesc']

def get_response(user_input):
    #iesirea din conversatie
    if user_input.lower() in exit_list:
        return "Ne auzim data viitoare!"

    #raspunsuri particulare/amuzante
    if user_input in ["Cum te numesti?","Care este numele tau?","Cum te cheama?"]:
        return "Ma numesc Bot Studi!"

    if user_input == "Ce faci?":
        return "Nu fac nimmic :) Astept intrebarile tale!"

    if "ceasul" in user_input:
        return "Ora este  " + current_time

    if "data" in user_input:
        return "Data curenta: " + str(azi)

    if "banc" in user_input:
        return random.choice(bancuri)

    if 'sunt facultatiile' in user_input:
        return "Acestea sunt:\nFacultatea de Electronica, Telecomunicatii si Tehnologii Informationale;" \
               "\nFacultatea de Automatica si Calculatoare" \
               "\nFacultatea de Constructii" \
               "\nFacultatea de Athitectura si Urbanism" \
               "\nFacultatea de Chimie Industriala si Ingineria Mediului" \
               "\nFacultatea de Electrotehnica si Electroenergetica" \
               "\nFacultatea de Inginerie din Hunedoara" \
               "\nFacultatea de Management in Productie si Transporturi" \
               "\nFacultatea de Mecanica" \
               "\nFacultatea de Stiinte ale Comunicarii"

    #raspunsurile generale
    if greeting_response(user_input) != None:
        return greeting_response(user_input)
    else:
        return bot_response(user_input)
