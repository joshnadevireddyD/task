FROM ubuntu:16.04
RUN apt-get update -y
RUN apt-get install -y python -y
RUN apt-get install python-pip -y
RUN pip install requests
RUN apt-get install python-pip
RUN pip install omdb
RUN pip install pystrich
ADD omdb.py /
ENTRYPOINT python omdb.py
