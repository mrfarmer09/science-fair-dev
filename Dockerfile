# Filename: Dockerfile
FROM tensorflow/tensorflow:latest-gpu
FROM nvidia/cuda:12.2.2-devel-ubuntu22.04
WORKDIR /home/science-fair-dev
RUN python3 -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
RUN wget https://github.com/mrfarmer09/science-fair-dev/blob/main/bash-scripts/docker-setup.sh && chmod +rwx docker-setup.sh && bash docker-setup.sh
EXPOSE 3000
