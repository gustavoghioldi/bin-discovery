From amancevice/pandas

COPY . /app
RUN pip install -r /app/requirements.txt

EXPOSE 8080
WORKDIR /app

CMD ["gunicorn", "-b", "127.0.0.1:8080", "app:app"]