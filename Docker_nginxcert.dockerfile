FROM nginx
MAINTAINER Mark Foley
RUN apt-get -y update && apt-get -y upgrade && apt-get -y install software-properties-common certbot python-certbot-nginx