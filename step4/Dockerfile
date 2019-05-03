FROM python:3.6

RUN apt update && apt install -y wait-for-it

RUN mkdir /code
COPY ./requirements.txt /code
RUN pip install -r /code/requirements.txt

ADD ./ /code

EXPOSE 5000
CMD wait-for-it -t 30 db:3306 && python /code/main.py
