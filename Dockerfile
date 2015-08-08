FROM ubuntu-upstart:14.04
MAINTAINER Gunjan Patel <gupatel@ciena.com>

#set mininet version
ENV MININET_VER 2.2.1rc1

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list \
 && apt-get update \
 && apt-get install -y git \
 && apt-get install -y python \ 


 && git clone https://github.com/mininet/mininet.git \
 && cd mininet \

 && git checkout -b 2.2.1rc1 \

 && cd .. \

 # ./mininet/util/install.sh -a




