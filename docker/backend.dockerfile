FROM debian:latest
LABEL maintainter="Partyzani hackatonski"

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install python python-pip

COPY requirements.txt /var/tmp
RUN pip install -r /var/tmp/requirements.txt
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8 HOME=/backend HOST=0.0.0.0 PORT=5000 FLASK_APP=/backend/main.py

ADD . ${HOME}

EXPOSE ${PORT}
WORKDIR ${HOME}

ENTRYPOINT flask run -h $HOST -p $PORT
