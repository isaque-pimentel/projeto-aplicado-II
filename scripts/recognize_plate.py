# Projeto Aplicado II - Recognize Plate

import pandas as pd
import numpy as np
import os
import tensorflow as tf
import plotly.express as px
import cv2
import pytesseract as pt

from tensorflow.keras.preprocessing.image import load_img, img_to_array
pt.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe" 
# Indicates the path the tesseract exe

# Set directory constants
file_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "dataset"
output_dir = "output"

# Create Plate Recognition Pipeline
def recognize_plate(path, show=False):
    # Load plate image
    plate_arr = np.array(load_img(test_plate_path))
    if show:
        fig = px.imshow(plate_arr)
        fig.update_layout(width=700, height=500, margin=dict(l=10, r=10, b=10, t=10))
        fig.show()
    # OCR using Tesseract
    plate_text = pt.image_to_string(plate_arr) # , lang='eng')
    return plate_text

# Load test plage image
test_dir = os.path.join(input_dir, "TEST")

filenames = ["TEST_1", "TEST_2", "TEST_3", "TEST_4"]

for filename in filenames:
    # Save test plate
    filename_plate = f"{filename}_PLATE"
    test_plate_path = os.path.join(test_dir, ".".join((filename_plate, "jpeg")))
    plate_text = recognize_plate(test_plate_path)
    print("Plate:"+fr"{plate_text}")