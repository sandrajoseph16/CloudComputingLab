# Code Lab 2
# Reference: https://stackoverflow.com/questions/27701930/how-to-add-users-to-docker-container
FROM python:3.7-alpine3.15
ENV useradd -ms /bin/bash newuser
docker run --name=test -d \
    --health-cmd='stat /etc/passwd || exit 1' \
    --health-interval=2s \
WORKDIR /usr/src/codelab2
COPY main.go go.* /src/
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv
# 2. Configure the system
# Run apt-get and install wget
RUN apt-get update 
RUN apt-get install -y wget