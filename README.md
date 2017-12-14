# Internet freedom in a Box
![charlie](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/charlie.png)

# Overview
> The​ ​“evil​ ​dictatorship​ ​in​ ​a​ ​box”​ ​is​ ​a​ ​project​ ​designed​ ​to​ ​allow​ ​contributors​ ​to 
> internet-freedom​ ​projects,​ ​developers​ ​of​ ​anti-censorship​ ​tools,​ ​researchers​ ​and​ ​anyone 
> interested​ ​in​ ​learning​ ​how​ ​the​ ​internet​ ​functions​ ​under​ ​repressive​ ​regimes​ ​to​ ​do​ ​so.​ ​It​ ​will 
> give​ ​its​ ​users​ ​the​ ​ability​ ​to​ ​accurately​ ​simulate​ ​the​ ​conditions​ ​placed​ ​on​ ​software​ ​and 
> technology​ ​users​ ​in​ ​countries​ ​and​ ​situations​ ​where​ ​government​ ​or​ ​dictators​ ​have​ ​complete 
> control. 
> In​ ​places​ ​where​ ​internet​ ​freedom​ ​and​ ​civil​ ​society​ ​are​ ​threatened,​ ​simply​ ​editing​ ​a 
> Wikipedia​ ​entry​ ​or​ ​chatting​ ​on​ ​IRC​ ​can​ ​be​ ​dangerous​ ​political​ ​actions.​ ​Reading​ ​a​ ​news​ ​app 
> or​ ​sharing​ ​video​ ​can​ ​be​ ​jailable​ ​offenses.

# Background
> This​ ​project​ ​was​ ​initially​ ​conceived​ ​of​ ​as​ ​part​ ​of​ ​the​ ​Push​ ​project,​ ​an​ ​open​ ​source​ ​mobile 
> news​ ​app​ ​ecosystem​ ​for​ ​small-​ ​and​ ​medium-sized​ ​news​ ​organizations.​ ​The​ ​initial​ ​Push 
> deployments​ ​were​ ​done​ ​in​ ​conjunction​ ​with​ ​the​ ​Organized​ ​Crime​ ​and​ ​Corruption​ ​Reporting 
> Project,​ ​a​ ​project​ ​working​ ​on​ ​its​ ​namesake​ ​in​ ​countries​ ​such​ ​as​ ​Russia,​ ​Azerbaijan,​ ​Moldova 
> and​ ​Serbia.​ ​These​ ​are​ ​countries​ ​where​ ​censorship,​ ​monitoring,​ ​or​ ​the​ ​spectre​ ​thereof​ ​is​ ​a 
> very​ ​real​ ​and​ ​daily​ ​occurrence.​ ​They​ ​are​ ​also​ ​quite​ ​technically-advanced​ ​and​ ​politically 
> threatened.​ ​Development​ ​of​ ​software​ ​tools​ ​that​ ​regular​ ​citizens​ ​and​ ​journalists​ ​can​ ​use​ ​on 
> a​ ​daily​ ​basis​ ​—​ ​for​ ​efforts​ ​as​ ​vast​ ​as​ ​breaking​ ​major​ ​news​ ​or​ ​releasing​ ​an​ ​investigative 
> project​ ​or​ ​as​ ​simple​ ​as​ ​contributing​ ​to​ ​a​ ​wiki​ ​and​ ​providing​ ​translations​ ​—​ ​is​ ​of​ ​paramount 
> interest​ ​and​ ​importance​ ​in​ ​these​ ​regions. ​
> 
> Push​ ​is​ ​currently​ ​supported​ ​by​ ​the​ ​Donald​ ​W.​ ​Reynolds​ ​Journalism​ ​Institute​ ​at​ ​the 
> University​ ​of​ ​Missouri​ ​Journalism​ ​School,​ ​along​ ​with​ ​previous​ ​contributions​ ​from​ ​the 
> International​ ​Center​ ​For​ ​Journalists.

# Goals
1. To​ ​build​ ​an​ ​open​ ​source​ ​project​ ​running​ ​ ​virtually​ ​or​ ​on​ ​end-user​ ​accessible 
hardware​ ​that,​ ​to​ ​various​ ​degrees,​ ​accurately​ ​represents​ ​the​ ​methodology​ ​and 
modality​ ​of​ ​censorship​ ​often​ ​deployed​ ​by​ ​repressive​ ​regimes. 
2. To​ ​build​ ​testing​ ​environments​ ​that​ ​allow​ ​the​ ​tweaking​ ​of​ ​Next​ ​Generation​ ​Firewall 
(NGFW)​ ​style​ ​tools​ ​to​ ​support​ ​open​ ​source​ ​contributors,​ ​editors,​ ​private​ ​citizens​ ​and 
developers​ ​when​ ​building​ ​anti-censorship​ ​projects. 
3. To​ ​empower​ ​the​ ​development​ ​of​ ​tools​ ​that​ ​give​ ​voice​ ​to​ ​civil​ ​society​ ​activists, 
journalists​ ​and​ ​everyday​ ​citizens​ ​living​ ​in​ ​and​ ​supporting​ ​populations​ ​in​ ​censored 
regimes​ ​and​ ​regions. 
4. To​ ​allow​ ​the​ ​tools​ ​to​ ​be​ ​simple​ ​to​ ​deploy​ ​on​ ​a​ ​local​ ​development​ ​environment​ ​but 
powerful​ ​enough​ ​that​ ​small-enterprise​ ​level​ ​hardware​ ​can​ ​also​ ​run​ ​the​ ​same​ ​tools 
for​ ​load​ ​and​ ​scale​ ​testing. 

# Project Structure

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

### Scapy
[Scapy Documentation](https://phaethon.github.io/scapy/api/usage.html#recipes)