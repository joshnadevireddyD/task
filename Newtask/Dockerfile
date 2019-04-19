FROM ubuntu:16.04
RUN apt-get update -y && \ 
    apt-get install -y python && \
    apt-get install -y python-pip && \
    apt-get install -y python-pip && \
    pip install requests && \
    pip install omdb && \
    pip install pystrich
ADD omdb.py /
ENTRYPOINT python omdb.py
