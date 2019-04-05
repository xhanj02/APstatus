FROM python:3.7.3-stretch

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY / /code/
EXPOSE 8000

CMD ["python", "main.py"]