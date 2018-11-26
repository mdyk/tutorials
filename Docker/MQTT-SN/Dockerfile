FROM ubuntu:latest

LABEL maintainer="Michal Dyk" \
    description="Eclipse Mosquitto MQTT-SN Gateway"

RUN apt-get update
RUN apt-get install -y git
RUN apt-get install -y make
RUN apt-get install -y g++
RUN apt-get install -y libssl-dev

EXPOSE 1883/udp
EXPOSE 1885/udp
EXPOSE 10000

RUN git config --global user.email "you@example.com"
RUN git config --global user.name mdyk
RUN git clone -b master https://github.com/eclipse/paho.mqtt-sn.embedded-c

WORKDIR paho.mqtt-sn.embedded-c

COPY . paho.mqtt-sn.embedded-c

USER root


RUN cd MQTTSNGateway && \
      make && \
      make install
      # make clean && \
      # cd ../ && \


RUN   cd MQTTSNGateway/Build && \
        ./MQTT-SNGateway -f ../../gateway.conf


#RUN MQTTSNGateway/Build/MQTT-SNGateway

#RUN cd MQTTSNGateway/GatewayTester && \
#    make && \
#    make install && \
#    ls -la && \
#    Build/MQTT-SNGatewayTester

