#tesorflow 1.14, CUDA 10.0, python 3.6.8, ubuntu 18.04.2 LTS
FROM tensorflow/tensorflow:1.14.0-gpu-py3

RUN pip install --upgrade pip

# nvidia-docker 1.0
LABEL com.nvidia.volumes.needed="nvidia_driver"
LABEL com.nvidia.cuda.version="${CUDA_VERSION}"

# nvidia-container-runtime
ENV NVIDIA_VISIBLE_DEVICES=all \
    NVIDIA_DRIVER_CAPABILITIES=compute,utility \
    NVIDIA_REQUIRE_CUDA="cuda>=8.0" \
    LANG=C.UTF-8

#kogpt-chatbot requirements
RUN pip3 install mxnet-cu101
RUN pip3 install mxnet gluonnlp sentencepiece pandas torch transformers pytorch_lightning 
RUN mkdir /KoGPT2chatbot
WORKDIR /KoGPT2chatbot
ADD . /KoGPT2chatbot
