FROM ubuntu:14.04
# This is from the ServerContainer
CMD echo "This is from the Server Container debian:lastest, Security-Onion"

# Update the server OS
RUN apt-get -y update
RUN apt-get -y upgrade

# Clean apt list repository
RUN rm -rf /var/lib/apt/lists/*
RUN apt-get update

# Install Common software onto distro
RUN apt-get -y install software-properties-common

# Add PPA repository to download security onion
RUN add-apt-repository -y ppa:securityonion/stable
RUN apt-get update

# Install Securityonion
RUN apt-get -y install securityonion-all syslog-ng-core
RUN sosetup

# Remove packages that are not longer needed
RUN apt-get -y autoremove 

RUN apt-get -y dist-upgrade

RUN apt-get clean

