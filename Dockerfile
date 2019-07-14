FROM python:3.5-slim

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3", "server.py"]