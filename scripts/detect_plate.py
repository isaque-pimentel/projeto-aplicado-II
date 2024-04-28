# Projeto Aplicado II - Detect Plate

import pandas as pd
import numpy as np
import os
import tensorflow as tf
import plotly.express as px
import cv2
import pytesseract as pt

from PIL import Image
from shutil import copy
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input
from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Set directory constants
file_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "dataset"
output_dir = "output"

# Load model
board_name = "object_detection"
model_filename = os.path.join(output_dir, ".".join((board_name, "keras")))
print(f"Load model from {model_filename}")
model = tf.keras.models.load_model(model_filename)
print("Model loaded successfully")


# Create pipeline
def detect_plate(path, verbose=False):
    # Read image
    image = load_img(path)  # PIL Object
    image = np.array(image, dtype=np.uint8)
    h, w, d = image.shape
    if verbose:
        print(f"Altura da imagem = {h}")
        print(f"Largura da imagem = {w}")
    # Data preprocessing
    load_image = load_img(test_path, target_size=(224, 224))
    load_image_arr = img_to_array(load_image) / 255.0
    test_arr = load_image_arr.reshape(1, 224, 224, 3)
    if verbose:
        print(f"Tamanho da imagem = {load_image_arr.shape}")
        print(f"Tamanho da imagem TEST (Input) = {test_arr.shape}")
    # Make prediction
    coords = model.predict(test_arr)
    # Denormalize
    denorm = np.array([w, w, h, h])
    coords = coords * denorm
    coords = coords.astype(np.int32)
    # Draw bounding on top the image
    xmin, xmax, ymin, ymax = coords[0]
    pt1 = (xmin, ymin)
    pt2 = (xmax, ymax)
    print(pt1, pt2)
    # Show test image with box
    cv2.rectangle(image, pt1, pt2, (0, 255, 0), 3)
    return image, coords

# Load test image
test_dir = os.path.join(input_dir, "TEST")
test_path = os.path.join(test_dir, "TEST.jpeg")
image, coords = detect_plate(test_path)
fig = px.imshow(image)
fig.update_layout(width=700, height=500, margin=dict(l=10, r=10, b=10, t=10))
fig.show()


# Save test plate
img_arr = np.array(load_img(test_path))
xmin, xmax, ymin, ymax = coords[0]
plate_arr = img_arr[ymin:ymax, xmin:xmax]
im = Image.fromarray(plate_arr)

test_plate_path = os.path.join(test_dir, "TEST_PLATE.jpeg")
im.save(test_plate_path)