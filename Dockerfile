FROM python:alpine
RUN pip install flask
COPY MainScores.py Score.py Utils.py ./app/
COPY ./templates/* ./app/templates/
CMD echo $((0 + $RANDOM % 1000)) > Scores.txt
WORKDIR /app
VOLUME /app/Scores.txt
EXPOSE 5000
ENTRYPOINT ["python", "/app/MainScores.py"]