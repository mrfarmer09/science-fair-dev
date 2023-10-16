# Filename: Dockerfile
FROM tensorflow/tensorflow:latest-gpu
WORKDIR /usr/src/asher-science-fair-dev
COPY * ./
RUN python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
COPY . .
EXPOSE 3000
