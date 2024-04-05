FROM python:3.12

WORKDIR /app

COPY main.py requirements.txt ./
COPY config ./config
COPY . ./

RUN apt-get update && apt-get install -y libgl1-mesa-glx && \
    pip3 install -U pip && pip3 install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
