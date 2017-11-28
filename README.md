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

![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/curlkibana.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/elastic-x-pack.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/elasticcurl.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/elasticlogin.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/elasticpass.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/elasticpassfail.png)
![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/kibanawithelastic.png)
