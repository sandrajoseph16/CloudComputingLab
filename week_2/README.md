## How to create a requirements.txt file from docker
- Run the docker file without the requirements.txt file 
```sh
docker build -t my_jupyter .
docker run -p8888:8888 my_jupyter
```
- Open notebook using the link on the terminal.
- Run the jupyter notebook and view the missing packages
- Launch another terminal and change directory to the docker file location. We will use this terminal to install the missing packages using root user.
To view the dockers running:
```sh
docker ps -a
```
Run following commands to install packages as root user:
```sh
docker exec -u 0 <container-name> pip install pandas
docker exec -u 0 <container-name> pip install seaborn
docker exec -u 0 <container-name> pip install sklearn
docker exec -u 0 <container-name> pip install pydotplus
docker exec -u 0 <container-name> pip install graphviz
```
- Run All cells in the jupyter file, no errors will occur
- From the jupyter file run the following command:
```sh
pip freeze > requirements.txt
```
- Return to the terminal and run the following command to copy the requirements.txt file to the local folder
```sh
docker cp <container-id>:app/notebooks/requirements.txt .
```

## How to run the Jupyter notebook on Docker container.
- To build the docker:
```sh
docker build -t my_jupyter .
```
- To run the docker container:
```sh
docker run -p8888:8888 my_jupyter
```
- Navigate to the notebooks folder in the jupyter tree 
- Open FinalProject.ipynb file

## To Check ownership of the files in the docker directory
- Check Jupyter notebook's cell first code cell
OR
- Launch terminal and change directory to the docker file location. And run the following commands.
To view the container name running:
```sh
docker ps -a
```
To execute a command:
```sh
docker exec -u sjoseph <container-name> ls -l /app/notebooks
```

## Reference links: 
<br>https://stackoverflow.com/questions/14093452/grep-only-the-first-match-and-stop 
<br>https://stackoverflow.com/questions/27701930/how-to-add-users-to-docker-container 
<br>https://askubuntu.com/questions/487527/give-specific-user-permission-to-write-to-a-folder-using-w-notation 
<br>https://stackoverflow.com/questions/22049212/docker-copying-files-from-docker-container-to-host 
<br>https://www.geeksforgeeks.org/copying-files-to-and-from-docker-containers/
