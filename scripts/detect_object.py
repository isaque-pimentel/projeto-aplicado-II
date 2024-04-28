# Projeto Aplicado II - Detect Object

import pandas as pd
import numpy as np
import os
import tensorflow as tf

from shutil import copy
from tensorflow.keras.models import Model
from tensorflow.keras.callbacks import TensorBoard
from sklearn.model_selection import train_test_split
from tensorflow.keras.applications import InceptionResNetV2
from tensorflow.keras.layers import Dense, Dropout, Flatten, Input

# Set directory constants
file_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "dataset"
output_dir = "output"

# Load model
board_name = "object_detection"
model_filename = os.path.join(output_dir, ".".join((board_name, "keras")))
print(f"Load model from {model_filename}")
model2 = tf.keras.models.load_model(model_filename)
print("Model loaded successfully")

test_path = os.path.join(input_dir, "TEST", "TEST.jpeg")
image = load_img(test_path)