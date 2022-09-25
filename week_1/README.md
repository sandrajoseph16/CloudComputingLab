1. To configure the docker and run the container use the following commands:<br />
docker build -t codelab1 <br />
docker run codelab1

2. To run the container in interactive mode. Use the following commands:<br />
docker build -t codelab1 <br />
docker container run -it codelab1 /bin/bash <br />
root@2687172d3388:/usr/src/assignment1# ls <br />
root@2687172d3388:/usr/src/assignment1# pwd <br />
root@2687172d3388:/usr/src/assignment1# cat company.txt <br />
