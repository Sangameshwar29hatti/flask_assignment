

# Flask CRUD Application with MongoDB

## Overview
This is a Flask application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database for a User resource using a REST API. The application is Dockerized for ease of deployment.

## Requirements
- Python 3.8+
- Docker
- Docker Compose

## Installation

### Cloning the Repository
First, clone the repository to your local machine:
```bash
git clone <repository-url>
cd flask_app


#docker-compose.yml

version: '3.8'

services:
  app:
    build: .
    ports:
      - "5000:5000"
    environment:
      MONGO_URI: "mongodb://mongo:27017/flask_db"
    depends_on:
      - mongo

  mongo:
    image: mongo
    ports:
      - "27017:27017"

Build and run the Docker containers:

docker-compose up --build


