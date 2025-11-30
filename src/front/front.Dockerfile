FROM python:3.11

WORKDIR /app

COPY app.py .
COPY templates ./templates
COPY static ./static

RUN pip install flask requests

CMD ["python", "app.py"]
