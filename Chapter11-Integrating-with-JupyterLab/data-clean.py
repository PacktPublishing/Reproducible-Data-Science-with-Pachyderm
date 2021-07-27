import nltk
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('wordnet')
nltk.download('punkt')
import re


stopwords = stopwords.words("english")
data = pd.read_csv("/pfs/data/data.csv", delimiter=",")

tokens = data['text'].apply(word_tokenize)
remove_stopwords = tokens.apply(lambda x: [w for w in x if w not in stopwords and w.isalpha()])
remove_urls = remove_stopwords.apply(lambda x: re.split('https:\/\/.*', str(x))[0])
remove_urls.to_csv('/pfs/out/cleaned-data.csv', index=True)

