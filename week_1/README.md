1. To configure the docker and run the container use the following commands:<br />
docker build -t codelab1 
docker run codelab1

2. To run the container in interactive mode. Use the following commands:<br />
docker build -t codelab1 
docker container run -it codelab1 /bin/bash
>ls
>pwd
>cat company.txt
