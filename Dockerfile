FROM python:3.12-slim

WORKDIR /app

COPY fetch_weather.py fetch_loop.py requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "fetch_loop.py"]
