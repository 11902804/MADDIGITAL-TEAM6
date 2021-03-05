FROM python:3.8-slim-buster
USER root
COPY . /app
WORKDIR /app 
RUN apt-get update && apt-get install -y software-properties-common libgl1-mesa-glx  libglib2.0-0 libssl-dev libffi-dev
RUN pip install --upgrade pip
RUN python -m pip install urllib3
RUN pip3 install -r requirements.txt
EXPOSE 6969
CMD uvicorn predict:app --reload --port 6969 --host 0.0.0.0 --ssl-keyfile ./local.key --ssl-certfile ./local.crt