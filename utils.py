from nltk.tokenize import word_tokenize
from nltk import PorterStemmer
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
import re
import string

# def Lema_word(s):
#     lema= WordNetLemmatizer()
#     return " ".join([lema.lemmatize(word) for word in s.split()])

def preprocessing(s):
    s=str.lower(s) # lower case
    s=re.sub("http\S+"," ",s) # removing http
    s=re.sub("[%s]" %re.escape(string.punctuation)," ",s) # removing punctuation
    s=re.sub("\n"," ",s) # removing \n
    # s=Lema_word(s) 
    s=re.sub(" +"," ",s) #Removing extra space
    return s