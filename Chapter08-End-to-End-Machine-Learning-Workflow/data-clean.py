from bs4 import BeautifulSoup
from urllib.request import urlopen
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')

with open('/pfs/data/data.txt', "r", encoding='utf-8') as f:
    data=f.read().replace('\n', '')
url = urlopen(data).read()
soup = BeautifulSoup(url, 'html.parser')
content = soup.get_text(strip=True)
paragraphs = soup.find_all('p')

f = open('/pfs/out/text.txt', 'w', encoding='utf-8')
for i in paragraphs:
    all_text = i.get_text()
    f.writelines(all_text)
f.close()

tokens = []
for i in paragraphs:
    tokens += word_tokenize(i.text)
    with open('/pfs/out/tokens.txt', 'w', encoding='utf-8') as filehandle:
        for item in tokens:
            filehandle.write('%s\n' % item)

stopwords = stopwords.words("english")
no_stopwords = []
for word in tokens:
     if not word in stopwords:
         no_stopwords.append(word)
         appendFile = open('/pfs/out/no_stopwords.txt', 'a', encoding='utf-8')
         appendFile.write(word)
         appendFile.write("\n")
         appendFile.close()

no_punctuation = []
for word in no_stopwords:
      if word.isalpha():
          no_punctuation.append(word)
          appendFile = open('/pfs/out/no_punctuation.txt', 'a', encoding='utf-8')
          appendFile.write(word)
          appendFile.write("\n")
          appendFile.close()

port_stem = PorterStemmer()
stemmed = []
for word in no_punctuation:
    stemmed_word = port_stem.stem(word)
    stemmed.append(stemmed_word)
    appendFile = open('/pfs/out/stemmed.txt', 'a', encoding='utf-8')
    appendFile.write(stemmed_word)
    appendFile.write("\n")
    appendFile.close()

lemmatizer = WordNetLemmatizer()
lemmatized = []
for word in no_punctuation:
    l_text = lemmatizer.lemmatize(word)
    lemmatized.append(l_text)
    appendFile = open('/pfs/out/lemmatized.txt', 'a', encoding='utf-8')
    appendFile.write(l_text)
    appendFile.write("\n")
    appendFile.close()

