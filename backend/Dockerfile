FROM python:3.13-alpine

WORKDIR /app


RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY ./apps /app

EXPOSE 8000

CMD ['python' 'manage.py' 'runserver' '0.0.0.0:8000']
