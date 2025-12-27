FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
COPY src/ ./src/
COPY src/main.py .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "main.py"]
