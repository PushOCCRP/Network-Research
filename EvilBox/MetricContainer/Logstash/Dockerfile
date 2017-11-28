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

ENV LOGSTASH_VERSION 5.2.1

# Add esuser to avoid starting Elasticsearch as the root user.
RUN adduser --disabled-password --gecos '' esuser
WORKDIR /home/esuser

RUN mkdir /data
RUN apt-get update && apt-get upgrade

# Install Logstash
RUN wget https://artifacts.elastic.co/downloads/logstash/logstash-${LOGSTASH_VERSION}.tar.gz \
        && tar -xzf logstash-${LOGSTASH_VERSION}.tar.gz

ENV PLUGIN /home/esuser/logstash-5.2.1/bin/logstash-plugin
RUN wget https://artifacts.elastic.co/downloads/packs/x-pack/x-pack-${LOGSTASH_VERSION}.zip

# # Install Elastisearch
# RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
#         && tar xvzf elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
#         && rm -f elasticsearch-${ELASTICSEARCH_VERSION}.tar.gz \
#         && chown -R esuser:esuser elasticsearch-${ELASTICSEARCH_VERSION}

#  # elasticsearch.yml and Dockerfile are on same location
#ADD kibana.yml /home/esuser/logstash-${LOGSTASH_VERSION}/config/kibana.yml
# #ENTRYPOINT elasticsearch-${ELASTICSEARCH_VERSION}/bin/elasticsearch
# #RUN touch /root/.bash_alias
# #RUN alias elasticsearch='/bin/elasticsearch ./elasticsearch' >> /root/.bash_alias
# ENV WORKDIR /home/esuser/logstash-${LOGSTASH_VERSION}-/bin
# USER esuser
# ENTRYPOINT cd ${WORKDIR} && ./kibana