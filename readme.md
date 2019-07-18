# Project purpose
This project provides simple endpoint that returns result of image classification as json.

# How to run
- install [Docker](https://www.docker.com/products/docker-desktop);
- pull image from Docker Hub by next command in console: `docker pull shnax0210/image_recognition`;
- create and run container from pulled image by next command in console: `docker run -p 5000:5000 --name image_recognition shnax0210/image_recognition`.

# How to use
- send jpg image as binary body to endpoint: `http://localhost:5000/api/predict` as POST request;
- by default it will return 5 results with max probabilities, but it can be changed by sending `number_of_results` parameter with new int value.