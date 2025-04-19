# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.13-bullseye

ENV ANDROID_HOME=/opt/android-sdk
ENV PATH=$ANDROID_HOME/cmdline-tools/latest/bin:$ANDROID_HOME/platform-tools:$PATH
ENV DEBIAN_FRONTEND=noninteractive

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \ 
    && apt-get install -y curl \
    && curl -fsSL https://deb.nodesource.com/setup_23.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt-get install -y nodejs

RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
ENV PATH=/root/.cargo/bin:$PATH

RUN apt -y install libwebkit2gtk-4.0-dev \
    build-essential \
    curl \
    wget \
    file \
    libxdo-dev \
    libssl-dev \
    libayatana-appindicator3-dev \
    librsvg2-dev

COPY . .

RUN pip3 --no-cache-dir install -r requirements.txt