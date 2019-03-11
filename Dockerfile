FROM python:3.7.2

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY main.py /main.py
COPY hostnames.db /hostnames.db
CMD ["python", "/main.py"]

RUN adduser -no-create-home user
USER user
