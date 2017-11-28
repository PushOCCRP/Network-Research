ServerContainer

* Folder Structure
	* Home
		* archive - version control
		* docker-compose.yml - spin up elastic, kibana and logstash
		* EvilBox - Entry point
			* images - store images of project 
			* MetricContainer 
				* Elasticsearch
					* elasticsearch.yml - config file for elasticsearch
					* Dockerfile - config to build container
				* ElkStack
					* elasticsearch.yml - config file for elasticsearch
					* Dockerfile - config to build container
				* Kibana
					* kibana.yml - config file for kibana
					* Dockerfile - config to build container
				* Logstash
					* logstash.yml - config file for logstash
					* logstash.simple.conf - listens for elasticsearch port 9200
					* Dockerfile - config to build container
			* ServerContainer
				* Bro
					* Dockerfile - config to build container
				* Dockerfile - config to build container

# To do Elastic Search
- [ ] install x-pack to /elasticsearch-5.2.1/bin/elastic-plugin install x-pack
- [ ] setup password for elasticsearch to get rid of login error
- [ ] Fix entrypoint in dockerfile, elasticsearch will only run if you attach to it manual.  Look at network in . yml file
- [ ] add volume for presist log storage

# Elastic Search Fix
- [x] localhost:9200 by attaching to container
- [x] localhost:9200 by running as deamon in background

# To do Kibana 
- [ ] install x-pack
- [ ] error ui-setting Elasticsearch plugin Red
- [ ] plugin elasticsearch unable to connect to localhost:9200
- [ ] add volume for presist log storage

# Kibana Fix
- [x] localhost:5601 by attaching to container
- [x] localhost:5601 by running as deamon in background

# To do logstash
- [ ] need to test
- [ ] add volume for presist log storage

