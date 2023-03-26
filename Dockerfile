FROM python:alpine
RUN pip install flask
COPY MainScores.py Score.py Utils.py ./app/
COPY ./templates/* ./app/templates/
WORKDIR /app
ENTRYPOINT ["python", "MainScores.py"]