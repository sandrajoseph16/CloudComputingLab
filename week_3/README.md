## How to run three components, a Database, a database Admin and a web frontend using Django

- Create a docker network for components to communicate with each other.
```sh
docker network create mynetwork
```
- Run PGAdmin on the network
- Change directory to DBA folder
```sh
cd DBA
docker build -t mydba .
docker run --name mydbacontainer --network mynetwork -p 8081:80 -d mydba
```

- Run Postgres DB on the network
- Change directory to DB folder
```sh
cd ../DB
docker build -t mydb .
docker run --name mydbcontainer --network mynetwork -itd -p 5432:5432 mydb 
```

- Go to localhost:8081 and login using Postgres 
Username: admin@admin.com
Password: pass

- Create a new server in Postgres and add the db using 'Add a server' option
- Set db name as 'mydbcontainer' 
Username: root
Password: pass

- Run Django container
- Change directory back to the home folder
```sh
cd ..
docker build -t mydjango .
docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app mydjango /bin/bash
```
- Go to localhost:8000/admin and login using 
Username: root
Password: pass

## How to Setup the Django container (web folder)
After building the django container using the following command:
```sh
docker build -t mydjango .
```
- Run the django container and map the system volume to the container volume without the network to first build the system:
```sh
docker run -it -p8000:8000 -v $(pwd)/app:/app mydjango /bin/bash
```
- Start the project from within the app volume: 
```sh
django-admin startproject web
```
- Apply all migrations to update and remove errors
```sh
python web/manage.py migrate
```

- Connect the Django container to the Postgres DB:
- Update settings.py to set the database from docker official django documentation
- Replace Database section with  the below docker code
```sh
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'web',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'mydbcontainer',
        'PORT': 5432,
    }
}
```

- Kill server and run again now connecting to the network this time and create a superuser to login to the localhost:8000
```sh
docker run -it -p8000:8000 --network mynetwork -v $(pwd)/app:/app mydjango /bin/bash
python web/manage.py migrate
python web/manage.py createsuperuser
# set email id as test@test.com and password as Pass
python web/manage.py runserver 0.0.0.0:8000
```
Navigate to localhost:8000/admin and login using username root, password: pass
All systems should be interconnected.
