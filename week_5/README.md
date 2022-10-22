## docker-compose to build an ‘api’ service and a “consumer” service using Flask 

## This application gives meals suggestion from a list of meals in a Postgres DB

- This folder contains mounted volumes of Postgres database called 'pgdata' and the Postgres DBAdmin session called 'pgadmin'

- To run this download the file on your local 
- Navigate to folder location 
```sh
cd week_5
```
- Run the docker-compose.yml file using the following command
```sh
docker-compose up
```
- To login to Postgres DB Admin console and view the database, navigate to http://localhost:5050
- Login using the following credentials
```sh
username: admin@admin.com 
password: pass
```
- You will be able to view the database and the Meals table.
- To view the api response go to http://localhost:5000 
- To get meal recommendations navigate to http://localhost:80

