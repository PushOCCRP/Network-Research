ServerContainer

* Folder Structure
	* Home
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
					*scripts - custom bro scripts 
				* Dockerfile - config to build container
		* archive - Old code
		* python_scripts - directory to hold scapy files
		* resources.txt - List of resources that were helpful in the development process

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

# To do Evilbox/ServerContainer/Bro
- [ ] need to mount scripts directory to dockerfile

# Resources
## BRO IDS

### Offical Documentation
[Bro offical Doc](https://www.bro.org/)

### Online Articles
[RyeSecurity](http://ryesecurity.blogspot.com/2012/05/learning-bro-scripting-language.html)
[HoldMyBeer](https://holdmybeer.xyz/2017/06/25/intro-to-threat-intelligence-with-bro-and-elk/)


### CheatSheet
[Bro Logs](/.https://github.com/corelight/bro-cheatsheets/blob/master/Corelight-Bro-Cheatsheets-2.5.pdf)

[Bro Syntax](./http://blog.bro.org/2011/11/bro-language-cheat-sheet.html)

[MarkDown](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf)