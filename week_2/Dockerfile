# Code Lab 2
# as of 9/29/2022 3.10.7 is the latest version
# Dockerfile that sets up basic container from python and install jupyter
FROM python:3.10.7
USER root
WORKDIR /app
RUN pip3 install jupyter

# from local folder copy requirements.txt to working directory and install the packages
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# create the new user and create a new directory
ENV JUPYTER_USER sjoseph 
RUN useradd -ms /bin/bash $JUPYTER_USER
RUN apt-get update && apt-get install -y wget 
RUN mkdir notebooks 

# Create new folder and use wget to save files into this new directory
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/FinalProject.ipynb
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/marketing_campaign.csv 

# set new user as the owner of all the files in the new directory
RUN chown -R $JUPYTER_USER:$JUPYTER_USER /app/notebooks
RUN chmod 755 /app/notebooks
EXPOSE 8888

# change user to the new user created.
USER ${JUPYTER_USER}
# run jupyter notebook on localhost
CMD jupyter notebook --ip=0.0.0.0 --port 8888 
