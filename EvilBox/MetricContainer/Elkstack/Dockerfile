## Elk Stack
FROM ubuntu:16.04

CMD "This is from the Metric Container debian:latest with ELk Stack"

# Update the System
RUN apt-get -y update && apt-get -y upgrade \
	software-properties-common \
	apt-transport-https \
	wget \
	curl \
	python-software-properties \
	debconf-utils \
	nano \
&& rm -rf /var/lib/apt/lists*

# Install Java
RUN add-apt-repository -y ppa:webupd8team/java \
	&& apt-get update \
	&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
	&& apt-get -y install oracle-java8-installer \
	&& apt-get autoremove

RUN useradd -d /home/esuser -m esuser
WORKDIR /home/esuser
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle

# Install elasticsearch
RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.0.0.tar.gz \
	&& sha1sum elasticsearch-6.0.0.tar.gz \
	&& tar -xzf elasticsearch-6.0.0.tar.gz \
	&& chown -R esuser:esuser elasticsearch-6.0.0

ADD elasticsearch.yml /home/esuser/elasticsearch-6.0.0/config/elasticsearch.yml
RUN elasticsearch-6.0.0/bin/elasticsearch -d 
RUN ps -p 1

#-Des.insecure.allow.root=true

#RUN /elasticsearch-6.0.0/bin/ ./elasticsearch

# elasticsearch.yml and Dockerfile are on same location

# ADD elasticsearch /etc/init.d
# RUN chmod 755 /etc/init.d/elasticsearch
# RUN update-rc.d elasticsearch defaults \
# 	&& service --status-all
#ENTRYPOINT elasticsearch-2.1.1/bin/elasticsearch

