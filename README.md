# IAonFiles

C'est le prototype de la détection de table et l'extraction de données, exploitable sur des documents tels que des fiches de paie, des factures etc.

## Option n°1 : Environnement (avec Dockerfile)

Lancer le Dockerfile

## Option n°2 : Environnement (sans Dockerfile)

- Installer `Python 3.10.12`

- Créer un environnement
``` bash
python -m venv env
```

- Activer l'environnement
  - Sur machine Linux/Ubuntu
  ``` bash
  source env/bin/activate
  ```
  
  - Sur machine Windows
  ``` bash
  ./env/Script/activate
  ```

- Installer toutes les librairies nécessaires
``` bash
!pip3 install -U timm requests opencv-python PyMuPDF pytesseract spacy
```

## Dataset

- Clôner un dataset de test, TableBank
``` bash
!git clone https://github.com/doc-analysis/TableBank.git
```

- Visualiser TableBank
``` bash
!echo "Images en Latex"
!ls -l /content/TableBank/data/Sampled_Detection_data/Latex/images

!echo "Images en Word"
!ls -l /content/TableBank/data/Sampled_Detection_data/Word/images
```
## Technologies

- Python
- Docker

## Ressources
### Programmation Python
- [Tracer une bounding box](https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/)
- [Passer de PDF à PNG](https://stackoverflow.com/questions/69643954/converting-pdf-to-png-with-python-without-pdf2image)
### Docker
- [Configurer un Dockerfile](https://docs.docker.com/guides/docker-concepts/building-images/writing-a-dockerfile/)
- [Activer un environnement virtuel dans un Dockerfile](https://pythonspeed.com/articles/activate-virtualenv-dockerfile/)
