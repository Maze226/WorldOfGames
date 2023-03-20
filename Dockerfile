FROM python:alpine

RUN pip install flask

COPY MainScores.py Score.py Utils.py Scores.txt ./

ENTRYPOINT ["python", "MainScores.py"]