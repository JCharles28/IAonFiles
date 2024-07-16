FROM python:3.10.12

WORKDIR ./app

# créer et lancer un environnement virturel
RUN python3 -m venv /opt/venv
RUN source ./env/bin/activate

# installation des librairies nécessaires (dans l'environnement)
COPY requirements.txt ./
RUN /opt/venv/bin/pip install --no-cache-dir -r requirements.txt


COPY src ./app/src
EXPOSE 8000

CMD ["python", "./app/src/rendu_dataleon.py"]
