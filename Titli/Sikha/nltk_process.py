import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from nltk.stem.snowball import SnowballStemmer

def preprocess_Text(sentence,matchWords1,matchWords2,matchWords3):
              sentence = sentence.lower()
              stemmer = SnowballStemmer("english")
              tokenizer = RegexpTokenizer(r'\w+')
              tokens = tokenizer.tokenize(sentence)
              Stop_words=set(stopwords.words('english'))
              Stop_words.update(('backup','r','n'))
              filtered_words = [w for w in tokens if not w in Stop_words]
              Data=" ".join(filtered_words)
              test=stemmer.stem(Data)
              test1=test.split()
              final = " ".join(set(test1))
              #print (final)   
              sumne = ['project1','asdf']
              if any(word in sentence for word in matchWords1):
                     return 1
              elif any(word in final for word in matchWords2):
                     return 2
              elif any(word in final for word in matchWords3):
                     return 3                     
                         
              else:
                     return 0   
              #return " ".join(set(test1))

#print (preprocess_Text("lets close the incident management dashboard with nice view"))

#print (preprocess_Text("i dont know how i got here but it is quite exciting"))
# l = ['servicenow','service now','service1']
# detailRequested = preprocess_Text("i would like to know details of service requests from bhp project and riotinto also would be good",l)

# print (detailRequested)
#print (preprocess_Text("asfasd asdfsd serviceasdf now"))


       

