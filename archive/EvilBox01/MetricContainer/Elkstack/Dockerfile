## Elk Stack
FROM ubuntu:16.04

CMD "This is from the Metric Container debian:latest with ELk Stack"

# Update the System
## Install packages
### Clean up after package installer
RUN apt-get -y update && apt-get -y upgrade \
	software-properties-common \
	apt-transport-https \
	wget \
	python-software-properties \
	debconf-utils \
	nano \
&& rm -rf /var/lib/apt/lists*

# Install Java
RUN add-apt-repository -y ppa:webupd8team/java \
	&& apt-get update \
	&& echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true" | debconf-set-selections \
	&& apt-get install -y oracle-java8-installer \
	&& apt-get autoremove \
	&& java -version 

# ElasticSearch repo added
## Get elasticsearch signed key
### Update and upgrade
RUN echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-5.x.list 
RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
	&& apt-get -y update && apt-get -y upgrade \
	&& apt-get -y install elasticsearch 

RUN update-rc.d elasticsearch defaults 95 10 \
	&& /etc/init.d/elasticsearch start \
	&& wget localhost:9200

RUN cat index.html \
	&& /etc/init.d/elasticsearch start \
	&& service --status-all

# RUN	apt-get -y install elasticsearch \
# 	&& service elasticsearch start \
# 	&& service --status-all

# RUN apt-get -y install kibana
# RUN bin/systemctl daemon-reload \
# 	&& bin/systemctl enable kibana.service \
# 	&& systemctl start kibana.service
# 	&& mkdir /home/gzipFiles

# RUN wget https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-5.2.0.deb -P /home/gzipFiles \
# 	&& dpkg -i elasticsearch-5.2.0.deb 
# 	#&& nano /etc/elasticsearch/elasticsearch.yml network.host:localhost
# 	#&& systemctl enable elasticsearch.service

# # Install Kibana
# RUN wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add - \
# 	&& apt-get install apt-transport-https \
# 	&& echo "deb https://artifacts.elastic.co/packages/5.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-5.x.list \
# 	&& apt-get update && sudo apt-get install kibana
	#nano /opt/kibana/config/kibana.yml