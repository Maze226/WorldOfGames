FROM python:alpine

RUN pip install flask

COPY MainScores.py Score.py Utils.py ./

VOLUME ./Scores.txt:/Scores.txt

ENTRYPOINT ["python", "MainScores.py"]