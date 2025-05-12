FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

#Copy project files
COPY . .

RUN chmod -R 777 /app

ENV PYTHONUNBUFFERED=1
