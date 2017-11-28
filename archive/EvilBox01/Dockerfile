## Elk Stack
FROM ubuntu:16.04

CMD "This is from the Metric Container debian:latest with ELk Stack"

# Update the System
RUN apt-get -y update && apt-get -y upgrade \
	software-properties-common \
	nano

# Install Java
RUN add-apt-repository -y ppa:webupd8team/java
RUN apt-get update
RUN apt-get -y install oracle-java8-installer

RUN apt-get update \
	&& mkdir /home/gzipFiles

RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.0.deb -P /home/gzipFiles \
	&& dpkg -i elasticsearch-5.2.0.deb 
	#&& nano /etc/elasticsearch/elasticsearch.yml network.host:localhost
	#&& systemctl enable elasticsearch.service

# Install Kibana
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - \
	&& apt-get install apt-transport-https \
	&& echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list \
	&& apt-get update && sudo apt-get install kibana
	#nano /opt/kibana/config/kibana.yml