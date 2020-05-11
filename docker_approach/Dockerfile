FROM mysql:5.5
MAINTAINER Adrian Vazquez "awsavazq@amazon.com"

ENV REFRESHED_AT 05-08-2020

ENV UBUNTU-FRONTEND noninteractive

ENV MYSQL_DATABASE crud_mono_flask
ENV MYSQL_USER dev
ENV MYSQL_PASSWORD dev
ENV MYSQL_RANDOM_ROOT_PASSWORD yes

## Cambiamos a root
USER root

#virtualenvwrapper setup
ENV  WORK_HOME=/workspace/envs
ENV  PROJECT_HOME=/workspace/dev

RUN apt-get -qq  update \
    && apt-get -y --allow-unauthenticated install python python-pip nano

## Templates para virtualenvwrapper
RUN mkdir -p ${WORK_HOME} && mkdir ${PROJECT_HOME}

ADD requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /tmp/requirements.txt
RUN echo "source /usr/local/bin/virtualenvwrapper.sh" >> /root/.profile

WORKDIR /app

COPY source_code/mb3/ /app

COPY database/ /docker-entrypoint-initdb.d/

##ENTRYPOINT ["python", "server.py"]
