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

RUN mkdir ./app

# Copying all file from outside folder to inside folder (in our case both are called apis)
COPY ./app ./app

COPY ./ ./

WORKDIR /app
# RUN performs a command execution on CMD, this one below installs Python requirements
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
