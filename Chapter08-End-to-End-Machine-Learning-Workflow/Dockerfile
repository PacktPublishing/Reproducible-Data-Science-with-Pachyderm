FROM python:3.8.3-slim

RUN apt-get update && apt-get install -y unixodbc-dev gcc
RUN apt-get update && apt-get -y install python3-pip

RUN pip3 install spacy==3.0.6
RUN python3 -m spacy download en
RUN python3 -m spacy download en_core_web_lg

RUN pip3 install nltk
RUN python3 -c 'import nltk; nltk.download("punkt"); nltk.download("stopwords")'

RUN pip3 install simplejson
RUN pip3 install "msgpack-numpy<0.4.4.0"
RUN pip3 install pathlib
RUN pip3 install urllib3
RUN pip3 install beautifulsoup4
RUN pip3 install ipython

ADD data-clean.py /data-clean.py
ADD ner-improved.py /ner-improved.py
ADD ner.py /ner.py
ADD pos-tag.py /pos-tag.py
ADD ner-my-model.py /ner-my-model.py
