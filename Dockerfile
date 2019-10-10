From python:3.7

COPY . /app

EXPOSE 8080
WORKDIR /app

RUN pip install -r requirements.txt 
CMD ["gunicorn", "-b", "127.0.0.1:8080", "app:app"]