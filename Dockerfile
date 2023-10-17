# Filename: Dockerfile
FROM tensorflow/tensorflow:latest-gpu
WORKDIR /home/science-fair-dev
COPY  ir tic-tac-toe
RUN python -c "import tensorflow as tf; print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
COPY . .
EXPOSE 3000
