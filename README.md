# IAonFiles

C'est le prototype de la détection de table et l'extraction de données, exploitable sur des documents tels que des fiches de paie, des factures etc.

## Environnement

- Installer Python
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
- Clôner un dataset de test, TableBank
``` bash
!git clone https://github.com/doc-analysis/TableBank.git
```
- Visualiser TableBank
```
!echo "Images en Latex"
!ls -l /content/TableBank/data/Sampled_Detection_data/Latex/images

!echo "Images en Word"
!ls -l /content/TableBank/data/Sampled_Detection_data/Word/images
```

## Technologies

- Python
- Docker

## Ressources
- [Tracer une bounding box](https://www.geeksforgeeks.org/python-opencv-cv2-rectangle-method/)
- [Passer de PDF à PNG](https://stackoverflow.com/questions/69643954/converting-pdf-to-png-with-python-without-pdf2image)
