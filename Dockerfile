# FROM python:3.11.2
# COPY . /app
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE $PORT
# CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

FROM python:3.11.2-slim-buster
# RUN apt-get update && apt-get install -y \
#     build-essential \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]