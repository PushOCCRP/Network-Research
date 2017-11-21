FROM ubuntu:16.04
# This is from the ServerContainer
CMD echo "This is from the Server Container Ubuntu:16.04, BRO installed /usr/local/bro"

# Update the server OS
RUN apt-get -y update && apt-get -y upgrade \
  software-properties-common \
  bison \
  cmake \
  flex \
  g++ \
  gdb \
  make \
  libmagic-dev \
  libpcap-dev \
  libgeoip-dev \
  libssl-dev \
  python-dev \
  swig2.0 \
  zlib1g-dev \
  wget \
  nano \
  git \
  gzip \
&& rm -rf /var/lib/apt/lists/*

RUN apt-get -y update \
  && mkdir /usr/share/gzipFiles

# Download geo file to /usr/share/gzipFiles
## Go to /usr/share/gzipFiles and decompress them
### mv files to /usr/share/GeoIP dir
RUN wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz -P /usr/share/gzipFiles \
  && wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz -P /usr/share/gzipFiles \
  && cd /usr/share/gzipFiles gzip -d GeoLiteCity.dat.gz gzip -d GeoIPCityv6.dat.gz \
  && cd /usr/share/gzipFiles/ mv GeoLiteCity.dat /usr/share/GeoIP/GeoIPCity.dat \
  && cd /usr/share/gzipFiles/ mv GeoLiteCityv6.dat /usr/share/GeoIP/GeoIPCityv6.dat

# Download and install BRO
RUN git clone --recursive git://git.bro.org/bro \
	&& cd bro \
	&& ./configure \
	&& make \
	&& make install 

ENV export PATH=/usr/local/bro/bin:$PATH

#CMD["broctl"]

## Need to configure this files



RUN apt-get -y update && apt-get -y autoremove


