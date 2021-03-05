FROM marvambass/nginx-ssl-secure
USER root
COPY ./dist/hdyftClient/ /usr/share/nginx/html/ 
COPY ./default.conf /etc/nginx/conf.d/
#RUN apt-get update && apt-get -y install curl
#RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
#RUN apt-get -y install nodejs
#WORKDIR /app
#RUN npm install --prefix /app
#RUN npm install -g @angular/cli
#RUN ng build --prod
#RUN cp -r /app/dist/hdyftClient/* 
#RUN cp /app/default.conf 
EXPOSE 443
