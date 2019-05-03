FROM python:3.6

RUN mkdir /code
COPY ./requirements.txt /code
RUN pip install -r /code/requirements.txt

ADD ./ /code

EXPOSE 5000
CMD python /code/main.py
