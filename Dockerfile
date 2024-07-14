FROM python:3.10.12

WORKDIR ./app


# installation des librairies nécessaires
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


COPY src ./app/src
EXPOSE 8000

CMD ["python", "./app/src/rendu_dataleon.py"]
