ARG CUDA_VERSION=11.8.0
FROM nvidia/cuda:${CUDA_VERSION}-base-ubuntu20.04 

ENV DEBIAN_FRONTEND noninteractive
WORKDIR /app

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        git \
        cmake \
        libsm6 \
        ffmpeg \
        python3 \
        libxext6 \
        python3-pip \
        libopencv-dev \
        libxrender-dev \
        build-essential \
        software-properties-common \
        && rm -rf /var/lib/apt/lists/* &&\
    python3 -m pip install -U pip &&\
    python3 -m pip install -U setuptools
COPY . .

RUN pip install -r requirements.txt
RUN pip install --user .
RUN chmod +x model/download_model.sh && bash model/download_model.sh && mkdir model && mv best.onnx model/

EXPOSE 8888
ENV MODEL_PATH="model/best.onnx"

CMD [ "python3", "app.py" ]
