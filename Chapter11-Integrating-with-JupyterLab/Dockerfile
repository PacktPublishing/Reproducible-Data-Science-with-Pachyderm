FROM python:3.8.3-slim

RUN apt-get update && apt-get -y install python3-pip

RUN pip3 install nltk
RUN python3 -c 'import nltk; nltk.download("punkt"); nltk.download("stopwords")'
RUN pip3 install pandas
RUN pip3 install scikit-image
RUN pip3 install matplotlib
RUN pip3 install seaborn
RUN pip3 install textblob
RUN python3 -m textblob.download_corpora

ADD data-clean.py /data-clean.py
ADD sentiment.py /sentiment.py
