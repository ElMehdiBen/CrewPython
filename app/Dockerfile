FROM python:3.8
# Below command to update and install additional needed packages
# RUN apt clean
# RUN apt-get update && apt-get install -y \
#     software-properties-common \
#     unzip \
#     curl \
#     xvfb

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Creating a directory called apis inside the container and set workdir
RUN mkdir /app
WORKDIR /app

COPY ./ ./

# RUN performs a command execution on CMD, this one below installs Python requirements
RUN pip3 install --no-cache-dir -r requirements.txt
