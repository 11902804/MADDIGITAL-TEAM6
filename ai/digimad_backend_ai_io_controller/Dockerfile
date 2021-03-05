FROM python:3.8-slim-buster
USER root
COPY . /app
WORKDIR /app
RUN pip3 install python-dotenv
RUN pip3 install -r requirements.txt
RUN pip3 install mysql-connector-python
RUN pip3 install uvicorn
RUN /bin/bash -c "source .env"
CMD uvicorn main:app --reload --port 8000 --host 0.0.0.0   --ssl-keyfile ./local.key --ssl-certfile ./local.crt