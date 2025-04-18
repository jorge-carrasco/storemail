# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.11-bullseye

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \ 
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get install -y nodejs

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt

