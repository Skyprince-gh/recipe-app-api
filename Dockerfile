# The first line of the doceker file is the image that we are going to inherit the docker file from
 FROM python:3.7-alpine

#  Specify who maintains this image
 MAINTAINER Ahenkan Kofi Akwa

#  Python unbuffered environment variables
ENV PYTHONUNBUFFERED 1

#copy requirement code from the requirements file adjacent to the docker file and copy it to requirements.txt in the docker image.
COPY ./requirements.txt /requirements.txt 

# use pip to run the instructions from the requirement file.
RUN pip install -r /requirements.txt 

# create an empty project directory on our docker image
RUN mkdir /app

# switch to the directory as your defualt directory specify the workspace
WORKDIR /app

# copy code from our local machine into the app folder
COPY ./app /app

# create user that is going to run our application in docker. This is done for security purposes.
RUN adduser -D user

# Switch docker from the user that we just created
USER user