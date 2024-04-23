FROM python:3.9-slim-bullseye
WORKDIR /api
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV APP_ENVIRONMENT=development
EXPOSE 8080
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080" ]
