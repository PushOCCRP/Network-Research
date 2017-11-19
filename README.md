ServerContainer

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
		![](https://github.com/PushOCCRP/Network-Research/blob/master/EvilBox/Images/customRboDirc.png)
		
