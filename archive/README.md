ServerContainer

Folder Structure
	- Home
		- archive - version control
		- docker-compose.yml - spin up elastic, kibana and logstash
		- EvilBox - Entry point
			- images - store images of project 
			- MetricContainer 
				- Elasticsearch
					- elasticsearch.yml - config file for elasticsearch
					- Dockerfile - config to build container
				- ElkStack
					- elasticsearch.yml - config file for elasticsearch
					- Dockerfile - config to build container
				- Kibana
					- kibana.yml - config file for kibana
					- Dockerfile - config to build container
				- Logstash
					-logstash.yml - config file for logstash
					- logstash.simple.conf - listens for elasticsearch port 9200
					- Dockerfile - config to build container
			- ServerContainer
				- Bro
					- Dockerfile - config to build container

				- * Dockerfile - config to build container


SecurityOnion Installed - Needs to be configured
![Unlimited Strength Jurisdiction](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/SecurityOnionServices.png)
	- When the container starts the security onions services are started
		- NSM
		- OSSEC-hids=server

	- Bro Directory
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/BRODirectory.png)
		- /nsm/bro/logs consumed by syslog-ng and stored in ELSA
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/BroLogFiles.png)

	- /opt/bro/share/bro/site - custome bro scripts
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/customBroDirc.png)
		
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/WeaverCloud.png)