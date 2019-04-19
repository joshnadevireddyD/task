FROM ubuntu:16.04
RUN apt-get update -y && \ 
    apt-get install python-pip -y && \
    pip install omdb  && \
    pip install requests 
ADD om_db.py /
ENTRYPOINT python om_db.py
