FROM onosproject/onos:1.2
MAINTAINER David Bainbridge <dbainbri@ciena.com>
COPY ./docker-entry-point.sh /docker-entry-point.sh
RUN chmod 755 /docker-entry-point.sh
ENTRYPOINT ["/docker-entry-point.sh"]
