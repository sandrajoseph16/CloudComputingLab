# Code Lab 2
# References: https://stackoverflow.com/questions/27701930/how-to-add-users-to-docker-container
# https://askubuntu.com/questions/487527/give-specific-user-permission-to-write-to-a-folder-using-w-notation
# https://stackoverflow.com/questions/22049212/docker-copying-files-from-docker-container-to-host
# https://www.geeksforgeeks.org/copying-files-to-and-from-docker-containers/
# as of 9/29/2022 3.10.7 is the latest version

#Dockerfile that sets up basic container from python and install jupyter
FROM python:3.10.7
USER root
RUN pip3 install jupyter
# RUN pip install pipreqs 
# && pip3 install -r requirements.txt
# RUN pip3 install pandas numpy

# Run apt-get and install wget
RUN apt-get update 
RUN apt-get install -y wget
#create a directory in the WORKDIR directory of the root user
WORKDIR /app
RUN mkdir notebooks
RUN cd notebooks
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/FinalProject.ipynb
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/marketing_campaign.csv 
# CMD jupyter trust FinalProject.ipynb
# create the new user and make them the owner of this new notebooks directory
ENV JUPYTER_USER sjoseph 
RUN useradd -ms /bin/bash ${JUPYTER_USER} 
RUN chown $JUPYTER_USER /app/notebooks

# RUN chmod u+w $HOME/notebooks
# RUN chmod r-x /app/notebooks
EXPOSE 8888

USER ${JUPYTER_USER}
# run jupyter notebook on localhost
 
CMD jupyter notebook --ip=0.0.0.0 --port 8888 
CMD jupyter trust FinalProject.ipynb



   ## && pip3 install -U setuptools && pip3 install utils\
   ## 
