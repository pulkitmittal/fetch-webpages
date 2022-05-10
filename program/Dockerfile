# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.8-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

# Install extra packages
RUN apt-get update && apt-get install firefox-esr -y
RUN apt-get install -y gosu

# verify that the binary works
RUN gosu nobody true

WORKDIR /fetch
COPY . /fetch

# Creates a user with an explicit UID and adds permission to access the /fetch folder
# gosu this user when running python script in entrypoint.sh
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /fetch

# Code file to execute when the docker container starts up (`entrypoint.sh`)
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/fetch/entrypoint.sh"]

CMD []