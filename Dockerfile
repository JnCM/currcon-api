FROM python:3.10-slim-buster

WORKDIR /currcon-api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "curr_converter/manage.py", "runserver", "0.0.0.0:8000"]
