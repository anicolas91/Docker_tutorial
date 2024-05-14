FROM python:3.10

# create working directory
WORKDIR /fastapi-app

# copy requirements into folder
COPY requirements.txt .

# install all requirements
RUN pip install -r requirements.txt

# copy app folder with main python file
COPY ./app ./app

# specify entrypoint to container
CMD ["python","./app/main.py"]

# to build the docker image:
# docker build -t python-fastapi .
# -t stands for tag

# to run the docker iamge as a container
# docker run -p 8000:8000 python-fastapi
# need to map the port 8000 from the outside to the 8000 on the container

#to list the running containers:
# docker ps

# to enter the container and see whats inside:
# docker exec -it idnumberofcontainer /bin/sh
# -it stands for interactive

# to exit the container hit ctrl+d