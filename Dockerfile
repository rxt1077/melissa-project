FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
