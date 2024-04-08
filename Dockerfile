# Use an official Python runtime as a base image
FROM python:3.10-slim

RUN apt-get update && apt-get upgrade
RUN apt-get install -y sqlite3 libsqlite3-dev

# Copy the dependencies file to the working directory
COPY requirements.txt ./

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY ./src ./src
COPY ./scripts .
COPY config.yaml config.yaml
COPY schema.sql schema.sql

RUN mkdir /logs
RUN touch /logs/telematics_service.log 

RUN mkdir /data
RUN touch /data/telematics.db 

# Expose the port the app runs on
EXPOSE 5000

# Define environment variables
ENV PYTHONUNBUFFERED=1

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Command to run the application
ENTRYPOINT ["./gunicorn_run.sh"]
