FROM python:3.11.1-alpine3.17

WORKDIR /home/project

COPY requirements.txt .

COPY ./app ./app

RUN ls

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]