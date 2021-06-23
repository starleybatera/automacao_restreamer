FROM python:3.7.3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt update && apt-get install libnss3 -y

RUN wget https://chromedriver.storage.googleapis.com/91.0.4472.101/chromedriver_linux64.zip && \
    python -m zipfile -e chromedriver_linux64.zip /usr/local/bin && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -f chromedriver_linux64.zip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .