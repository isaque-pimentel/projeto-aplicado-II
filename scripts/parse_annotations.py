# Projeto Aplicado II - Parse Annotations to CSV

import pandas as pd
import xml.etree.ElementTree as xet
import os

from glob import glob

# Set directory constants
file_dir = os.path.dirname(os.path.relpath(__file__))
input_dir = "dataset"
output_dir = "output"

path = glob(input_dir + r"\annotations\*.xml")

label_d = {
    "filepath": [],
    "xmin": [],
    "xmax": [],
    "ymin": [],
    "ymax": [],
    "image_path": [],
}

for filename in path:
    tree = xet.parse(filename)
    root = tree.getroot()

    object = root.find("object")
    box = object.find("bndbox")

    # Collect plate location
    xmin = int(box.find("xmin").text)
    xmax = int(box.find("xmax").text)
    ymin = int(box.find("ymin").text)
    ymax = int(box.find("ymax").text)

    # Collect image relative path
    folder_name = root.find("folder").text
    image_name = root.find("filename").text
    image_name = os.path.join(input_dir, folder_name, image_name)

    label_d["filepath"].append(filename)
    label_d["xmin"].append(xmin)
    label_d["xmax"].append(xmax)
    label_d["ymin"].append(ymin)
    label_d["ymax"].append(ymax)
    label_d["image_path"].append(image_name)


# Show the dataframe
df = pd.DataFrame(label_d)
print(df.head())

# Save the dataframe into a csv file
csv_filename = output_dir + r"\labels.csv"
print(csv_filename)
df.to_csv(csv_filename, index=False)
