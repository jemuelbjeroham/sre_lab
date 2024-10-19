FROM python:3.8-slim
RUN pip install Flask
COPY app.py /app/app.py
WORKDIR /app
CMD ["python", "app.py"]
