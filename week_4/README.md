# docker-compose to build an ‘api’ service and a “consumer” service using Flask

## This application gives meals suggestion from a list of meals in the JSON file

- To run this download the directory on your local 
- Navigate to folder location 
```sh
cd week_4
```
- Run the docker-compose.yml file using the following command
```sh
docker-compose up
```
- Go to http://localhost:80
- Close the docker compose and check the volumes: Run the following command for each docker:
- Run week_4-api docker
```sh
docker run -it -p5000:5000 -v $(pwd)/api/code:/app week_4-api /bin/bash
pwd
ls
```
all files in code will be listed

- Exit and - Run week_4-consumer docker:
```sh
docker run -it -p5000:5000 -v $(pwd)/api/code:/app week_4-consumer /bin/bash
pwd
ls
```
all files in code will be listed
