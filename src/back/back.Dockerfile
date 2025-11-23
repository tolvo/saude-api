FROM python:3.11

WORKDIR /app/back

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY database.py .
COPY routes/ ./routes/

CMD ["python", "app.py"]
