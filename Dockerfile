FROM python:alpine
RUN pip install flask
COPY MainScores.py Score.py Utils.py Scores.txt ./app/
COPY ./templates/* ./app/templates/
WORKDIR /app
VOLUME /app/Scores.txt
EXPOSE 5000
ENTRYPOINT ["python", "/app/MainScores.py"]