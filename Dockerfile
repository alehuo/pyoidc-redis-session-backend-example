FROM python:3.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN pip install -i https://test.pypi.org/simple/ pyoidc-redis-session-backend-alehuo==1.0.7

COPY src ./src

EXPOSE 5000

WORKDIR /app/src

CMD python3 app.py
