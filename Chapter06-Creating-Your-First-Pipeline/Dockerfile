FROM ubuntu:18.04

RUN apt-get update && apt-get install -y tzdata
ENV TZ=US/Pacific
RUN ln -fs /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get -y install python3.8 python3-pip

RUN pip3 install scikit-image
RUN pip3 install numpy
RUN pip3 install matplotlib

ADD histogram.py /histogram.py
ADD contour.py /contour.py
