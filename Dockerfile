FROM python:3.12-slim
LABEL authors="Thomas Chambon"

WORKDIR /usr/src/app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

RUN useradd -m myuser
USER myuser

EXPOSE 8000

CMD ["python3", "main.py"]