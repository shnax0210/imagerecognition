FROM python:3.5-slim

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
RUN python3 -c "exec(\"from vgg19 import VGG19\nmodel = VGG19(weights='imagenet')\")"

EXPOSE 5000

ENTRYPOINT ["python3", "server.py"]