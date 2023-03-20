FROM python:alpine

RUN pip install flask


COPY MainScores.py Score.py Utils.py Scores.txt ./

EXPOSE 80

ENTRYPOINT ["python", "MainScores.py"]