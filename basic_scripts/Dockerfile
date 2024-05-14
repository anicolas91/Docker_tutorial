# blueprint for building images

FROM python:3.8

ADD main.py .

RUN pip install torch numpy

# strings need to always be ""
CMD [ "python","./main.py" ]

#to build docker image:
    # docker build -t snek:v1 .
    # t is for version
# to run container:
    #docker run snek