# Code Lab 1
# Reference links: 
# https://stackoverflow.com/questions/14093452/grep-only-the-first-match-and-stop
# https://phoenixnap.com/kb/docker-run-command-with-examples
# To run this file 
# the container in interactive mode. Use the following commands:
# docker build -t codelab1 
# docker container run -it codelab1 /bin/bash
# ls
# pwd
# cat company.txt

# 1. Setup a docker container
FROM python:latest
WORKDIR /usr/src/codelab1

# 2. Configure the system
# Run apt-get and install wget
RUN apt-get update 
RUN apt-get install -y wget

# 3. Do something with the system
# Download the raw version of csv from the source location,
RUN wget https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv

# 3. Search for company name in the file using regex
# Once company name is extracted using grep command, it is stored in company.txt folder 
RUN grep -o -m 1 "\w* INC\b" fb_sub.csv > company.txt
# Print contents of company.txt file when the container is run.
# Use command: docker run codelab1
CMD ["cat","company.txt"]


