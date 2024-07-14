from transformers import DetrImageProcessor, DetrForObjectDetection
import torch
from PIL import Image
import requests, os, cv2, fitz, pytesseract, spacy
from google.colab.patches import cv2_imshow
import numpy as np

# Model
processor = DetrImageProcessor.from_pretrained("TahaDouaji/detr-doc-table-detection")
model = DetrForObjectDetection.from_pretrained("TahaDouaji/detr-doc-table-detection")

# Dataset
print("Images en Latex")
for root, dirs, files in os.walk("/TableBank/data/Sampled_Detection_data/Latex/images"):
    for name in files:
        file_path = os.path.join(root, name)
        print(file_path)

print("Images en Latex")
for root, dirs, files in os.walk(/TableBank/data/Sampled_Detection_data/Word/images):
    for name in files:
        file_path = os.path.join(root, name)
        print(file_path)


# Classe IAonFiles
class IAonFiles:

  def __init__(self, model, rep, image):
    self.model = model  # modèle
    self.rep = rep  # répertoire d'images
    self.image = image  # image

  def detect(self, image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = self.model(**inputs)

    target_sizes = torch.tensor([image.size[::-1]])
    results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.8)[0]

    image_numpy = np.array(image)

    for score, label, box in zip(
                                  results["scores"],
                                  results["labels"],
                                  results["boxes"]
                                ):
        box = [round(i, 2) for i in box.tolist()]
        libelle = model.config.id2label[label.item()]
        print(
                f"Detected {libelle} with confidence \n"
                f"{100*round(score.item(), 3)}% at location {box}"
        )

        self.get_box_label(image_numpy, box, label=libelle, color=(0,0,255), txt_color=(255, 255, 255))

    # affichage de l'image détectée
    cv2_imshow(image_numpy)

    # sauvegarder l'image
    cv2.imwrite('/output/output.png', image_numpy)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

  def detect_rep(self, rep):
    for root, dirs, files in os.walk(rep):
      for name in files:
          file_path = os.path.join(root, name)
          print(file_path)
          img = Image.open(file_path)
          self.detect(img)

  def detect_pdf(self, file_path):
    doc = fitz.open(file_path)
    for i, page in enumerate(doc):

        # transforme une page du pdf en image
        pix = page.get_pixmap()

        # sauvegarde chaque page
        pix.save(f"page_{i}.png")
        image = Image.open(f"./output/page_{i}.png")
        self.detect(self.model, image)

  def get_box_label(self, image, box, label='', color=(128, 128, 128), txt_color=(255, 255, 255)):
    lw = max(round(sum(image.shape) / 2 * 0.003), 2)
    p1, p2 = (int(box[0]), int(box[1])), (int(box[2]), int(box[3]))
    cv2.rectangle(image, p1, p2, color, thickness=2, lineType=cv2.LINE_AA)
    if label:
      tf = max(lw - 1, 1)
      # paramétrage du libellé
      w, h = cv2.getTextSize(label, 0, fontScale=lw / 3, thickness=tf)[0]

      outside = p1[1] - h >= 3
      p2 = p1[0] + w, p1[1] - h - 3 if outside else p1[1] + h + 3

      # traçage de box + libellé
      cv2.rectangle(image, p1, p2, color, -1, cv2.LINE_AA)
      cv2.putText(image,
                  label, (p1[0], p1[1] - 2 if outside else p1[1] + h + 2),
                  0,
                  lw / 3,
                  txt_color,
                  thickness=tf,
                  lineType=cv2.LINE_AA)


# Test (RUN)

img_test = Image.open("/TableBank/data/Sampled_Detection_data/Latex/images/1401.0007_5.jpg")
rep_test = "/TableBank/data/Sampled_Detection_data/Latex/images"

# instance de la classe
IA  = IAonFiles(model, rep_test, img_test)

# test des fonctionnalité de la classe
IA.detect(img_test)
IA.detect_rep(rep_test)

