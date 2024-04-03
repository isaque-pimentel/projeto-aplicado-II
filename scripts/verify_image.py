# Projeto Aplicado II - Verify the Labelling for an Image

import pandas as pd
import os
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
from skimage import io

# Set directory constants
file_dir = os.path.dirname(os.path.relpath(__file__))
input_dir = "dataset"
output_dir = "output"

# Load the dataframe from a csv file
csv_filename = output_dir + r"\labels.csv"
print(csv_filename)
df = pd.read_csv(csv_filename)

# Show the dataframe
print(df.head())

# Choose the image here
image_idx = 10
file_path = df["image_path"].iloc[image_idx]

# Read the image
img = io.imread(file_path)
fig = px.imshow(img)
fig.update_layout(
    width=600,
    height=500,
    margin=dict(l=10, r=10, b=10, t=10),
    xaxis_title="Figure 8 - N2.jpeg with bounding box",
)

fig.show()

# # Add the label
# fig.add_shape(
#     type="rect", xref="x", line_color="red", x0=xmin, x1=xmax, y0=ymin, y1=ymax
# )
