# Project purpose
This project allows to get more benefits from three point estimation. 
For details please refer to base [notebook](https://github.com/shnax0210/work_estimation/blob/master/base_estimation.ipynb).

# How to run
- install [Docker](https://www.docker.com/products/docker-desktop);
- pull image from Docker Hub by next command in console: `docker pull shnax0210/image_recognition`;
- create and run container from pulled image by next command in console: `docker run -p 5000:5000 --name image_recognition shnax0210/image_recognition`.

# How to use
- send jpg image as binary body to endpoint: `http://localhost:5000/api/predict` as POST request.
