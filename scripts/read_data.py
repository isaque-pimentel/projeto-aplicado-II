# Projeto Aplicado II - Read Data

import pandas as pd
import numpy as np
import os
import cv2

from tensorflow.keras.preprocessing.image import load_img, img_to_array

# Set directory constants
file_dir = os.path.dirname(os.path.abspath(__file__))
input_dir = "dataset"
output_dir = "output"

# Load the dataframe from a csv file
csv_filename = os.path.join(output_dir, "labels.csv")
print(csv_filename)
df = pd.read_csv(csv_filename)

# Show the dataframe
print(df.head())

# Set labels and image_paths
labels = df[["xmin", "xmax", "ymin", "ymax"]].to_numpy()
image_paths = df["image_path"]

# Read data
data = []
output = []
for image_path, label in zip(image_paths, labels):
    # Read using CV2
    img_arr = cv2.imread(image_path)
    h, w, d = img_arr.shape
    # Preprocessing: Normalizing to image
    load_image = load_img(image_path, target_size=(224, 224))
    load_image_arr = img_to_array(load_image)
    norm_load_image_arr = load_image_arr / 255.0
    # Normalizing to label
    xmin, xmax, ymin, ymax = label
    nxmin, nxmax = xmin / w, xmax / w
    nymin, nymax = ymin / h, ymax / h
    label_norm = nxmin, nxmax, nymin, nymax
    # Add to data, output
    data.append(norm_load_image_arr)
    output.append(label_norm)

# Convert data, label to array
X = np.array(data, dtype=np.float32)
y = np.array(output, dtype=np.float32)

# Dump to a npy file
dump_filename = os.path.join(output_dir, "X")
print(f"Dumping X into {dump_filename}")
np.save(dump_filename, X)

dump_filename = os.path.join(output_dir, "y")
print(f"Dumping y into {dump_filename}")
np.save(dump_filename, y)
