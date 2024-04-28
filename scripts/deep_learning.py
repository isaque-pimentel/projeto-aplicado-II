# Projeto Aplicado II - Read Data

import pandas as pd
import numpy as np
import os
import cv2
import tensorflow as tf
import plotly.express as px

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

# Load the dataframe from a csv file
csv_filename = output_dir + r"\labels.csv"
print(csv_filename)
df = pd.read_csv(csv_filename)

# Load data
load_filename = os.path.join(output_dir, ".".join(("X", "npy")))
print(f"Loading X from {load_filename}")
X = np.load(load_filename)

# Split training/test data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=0.8, random_state=0
)
print(f"Formato de X_train: {X_train.shape}")
print(f"Formato de X_test: {X_test.shape}")
print(f"Formato de y_train: {y_train.shape}")
print(f"Formato de y_test: {y_test.shape}")

# Deep Learning Model: INCEPTION RESNET V2

inception_resnet = InceptionResNetV2(
    weights="imagenet", include_top=False, input_tensor=Input(shape=(224, 224, 3))
)

# Output model
headmodel = inception_resnet.output
headmodel = Flatten()(headmodel)
headmodel = Dense(500, activation="relu")(headmodel)
headmodel = Dense(250, activation="relu")(headmodel)
# Corresponding to xmin, xmax, ymin, ymax
headmodel = Dense(4, activation="sigmoid")(headmodel)

# Build model
model = Model(inputs=inception_resnet.input, outputs=headmodel)

# Compile model
model.compile(loss="mse", optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4))
model.sumary()

# Training model and Save
