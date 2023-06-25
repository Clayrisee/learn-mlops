ARG CUDA_VERSION=11.8.0
FROM nvidia/cuda:${CUDA_VERSION}-base-ubuntu20.04 

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y


RUN apt update -q \
    && apt install -yq python3-pip libcurl3-gnutls curl rsync libssl-dev libcurl4-openssl-dev libcurl4 git gcc libssh2-1 libpq-dev libpopt0 \
    && ln -s /usr/bin/python3 /usr/bin/python \
    && pip install --upgrade pip --default-timeout=1000 \
    && pip install --upgrade --force-reinstall --user setuptools 



RUN apt install -yq curl \
    && curl -sL https://deb.nodesource.com/setup_14.x -o nodesource_setup.sh \
    && bash nodesource_setup.sh \
    && apt install -yq nodejs 

ENV PATH="${PATH}:/root/.local/bin"

# RUN pip install --user pip "jupyterlab>=3" "ipywidgets>=7.6,<8"

RUN pip install --user "jupyterlab==3.6.1" ipympl "plotly==5.13.1"

WORKDIR /app/
COPY dataset-utils dataset-utils
COPY requirements.txt /app/requirements.txt
COPY entrypoints.sh /app/entrypoints.sh

RUN pip --default-timeout=1000 install --user -r requirements.txt