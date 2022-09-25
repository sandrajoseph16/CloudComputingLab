Reference links: <br />
https://stackoverflow.com/questions/14093452/grep-only-the-first-match-and-stop <br />
https://phoenixnap.com/kb/docker-run-command-with-examples

1. To configure the docker and run the container use the following commands:<br />
docker build -t codelab1 <br />
docker run codelab1

2. To run the container in interactive mode. Use the following commands:<br />
docker build -t codelab1 <br />
docker container run -it codelab1 /bin/bash <br />
ls <br />
pwd <br />
cat company.txt <br />
