FROM python
RUN pip3 install flask
RUN pip3 install psycopg2
RUN pip3 install sqlalchemy
ENV API_HOST=${API_HOST}
ENV API_PORT=${API_PORT}
VOLUME [ "/app" ]
WORKDIR /app
EXPOSE ${API_PORT}

