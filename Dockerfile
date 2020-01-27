FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src ./src

EXPOSE 5000

WORKDIR /app/src

CMD python3 app.py
