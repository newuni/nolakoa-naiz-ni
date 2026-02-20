FROM python:3.14-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn httpx

COPY backend.py .
COPY static/ static/

EXPOSE 8096

CMD ["uvicorn", "backend:app", "--host", "0.0.0.0", "--port", "8096"]
