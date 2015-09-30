FROM ubuntu
RUN apt-get update && \
    apt-get install -y libxml2-dev libxslt1-dev python-dev python
RUN apt-get install -y python-pip
#RUN apt-get install -y lib32z1-dev
RUN apt-get install -y python-lxml

WORKDIR /srv
ADD requirements.txt /srv/
RUN pip install -r requirements.txt
ADD . /srv/
CMD ['/bin/bash']
