FROM python:3.8.3-slim

RUN apt-get update && apt-get install -y unixodbc-dev gcc
RUN apt-get update && apt-get -y install python3-pip

RUN pip3 install joblib
RUN pip3 install pandas
RUN pip3 install seaborn
RUN pip3 install matplotlib
RUN pip3 install numpy
RUN pip3 install sklearn

ADD data-explore.py /data-explore.py
ADD data-clean.py /data-clean.py
ADD outliers.py /outliers.py
ADD train.py /train.py
ADD grid-search.py /grid-search.py
