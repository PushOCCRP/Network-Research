FROM ubuntu:16.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get -y update && apt-get -y upgrade \
        default-jre \
        build-essential \
        software-properties-common \
        curl \
        git \
        wget \
        nano \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get autoremove

ENV ELASTICSEARCH_VERSION 5.2.1
# Add esuser to avoid starting Elasticsearch as the root user.
RUN adduser --disabled-password --gecos '' esuser
WORKDIR /home/esuser

RUN mkdir /data

# Install Elastisearch
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
        && tar xvzf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
        && rm -f elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
        && chown -R esuser:esuser elasticsearch-${ELASTICSEARCH_VERSION}

 # elasticsearch.yml and Dockerfile are on same location
ADD elasticsearch.yml /home/esuser/elasticsearch-${ELASTICSEARCH_VERSION}/config/elasticsearch.yml
ENV WORKDIR /home/esuser/elasticsearch-5.2.1/bin

# Install X-pack
RUN cd ${WORKDIR} && ./elasticsearch-plugin install x-pack

# Have to change to esuser because can not run elastic as root
USER esuser

ENTRYPOINT cd /home/esuser/elasticsearch-5.2.1/bin \
         && ./elasticsearch

################### WORKS #######################################################################

#RUN ${WORKDIR}
#USER esuser
#ENTRYPOINT cd ${WORKDIR} && ./elasticsearch
#ENTRYPOINT ./elasticsearch
#RUN whoami