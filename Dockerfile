FROM ubuntu
RUN apt-get update && \
    apt-get install -y \
    	libxml2-dev libxslt1-dev lib32z1-dev \
    	python-dev python python-pip

WORKDIR /srv
ADD requirements.txt /srv/
RUN pip install -r requirements.txt

ADD . /srv/
CMD ['/bin/bash']
