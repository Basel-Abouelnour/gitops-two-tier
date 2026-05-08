FROM python:3.11.15-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY frontend.py .
EXPOSE 3000
CMD ["python", "frontend.py"]

