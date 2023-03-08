FROM python:alpine

RUN pip install flask

COPY . .

ENTRYPOINT ["python", "MainScores.py"]