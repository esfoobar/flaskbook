#
# ZeroTribe Dockerfile
#
#

# Pull base image.
FROM centos:7.2.1511

# Build commands
ENV PYTHONUNBUFFERED 1
RUN yum -y update; yum clean all
RUN yum install -y python-setuptools gcc gcc-c++ python-devel ImageMagick-devel; yum clean all
RUN echo -e "[mongodb-org-3.0] \n\
name=MongoDB Repository \n\
baseurl=http://repo.mongodb.org/yum/redhat/\$releasever/mongodb-org/3.0/x86_64/ \n\
gpgcheck=0 \n\
enabled=1" >> /etc/yum.repos.d/mongodb-org-3.0.repo
RUN yum install -y mongodb-org; yum clean all
RUN easy_install pip
RUN mkdir /opt/flaskbook
WORKDIR /opt/flaskbook
ADD requirements.txt /opt/flaskbook/
RUN pip install -r requirements.txt
ADD . /opt/flaskbook

# start the app server
CMD python manage.py runserver
