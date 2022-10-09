# create a docker from python
FROM python
# to get the django framework do a pip. 
# its good to have the 
COPY requirements.txt /tmp/  
RUN pip3 install -r /tmp/requirements.txt
# we notify to expect a volume in the app directory.
VOLUME /app  
WORKDIR /app

EXPOSE 8000

