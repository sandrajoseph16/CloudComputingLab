# Code Lab 2
# as of 9/29/2022 3.10.7 is the latest version
# Dockerfile that sets up basic container from python and install jupyter
FROM python:3.10.7
USER root
WORKDIR /app
RUN pip3 install jupyter

# from local folder copy requirements.txt to working directory
COPY requirements.txt /app
RUN pip3 install -r requirements.txt

# Create new folder and use wget to save files into this new folder
RUN apt-get update 
RUN apt-get install -y wget
RUN mkdir notebooks
RUN cd notebooks
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/FinalProject.ipynb
RUN wget -P notebooks/ https://raw.githubusercontent.com/sandrajoseph16/CloudComputingLab/main/week_2/marketing_campaign.csv 

# create the new user and make them the owner of this new notebooks directory
ENV JUPYTER_USER sjoseph 
RUN useradd -ms /bin/bash ${JUPYTER_USER} 
RUN chown $JUPYTER_USER:$JUPYTER_USER /app/notebooks
EXPOSE 8888
# change user to the new user created.
USER ${JUPYTER_USER}
# run jupyter notebook on localhost
CMD jupyter notebook --ip=0.0.0.0 --port 8888 
