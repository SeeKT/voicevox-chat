FROM nvidia/cuda:12.0.0-cudnn8-devel-ubuntu22.04
RUN DEBIAN_FRONTEND=noninteractive
RUN ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime

## Install packages
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install \ 
    software-properties-common \
    build-essential \
    wget && \
    rm -rf /var/lib/apt/lists*

## Add Python 3.10
RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update
RUN apt-get install -y python3.10 python3-pip


## Install packages
ENV PATH=$PATH:/usr/local/cuda-12.0/bin \
    CMAKE_ARGS="-DLLAMA_CUBLAS=on" \
    LLAMA_CUBLAS=1 \
    FORCE_CMAKE=1
RUN pip install --upgrade pip
RUN pip install llama-cpp-python --upgrade --force-reinstall --no-cache-dir -vv
RUN pip install llama-cpp-python[server] --upgrade --force-reinstall --no-cache-dir -vv
RUN pip install langchain langchain-community


## Set Workdir
WORKDIR /app 

COPY . .