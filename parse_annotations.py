# Projeto Aplicado II - Parse Annotations to CSV

import pandas as pd
import xml.etree.ElementTree as xet
import os

from glob import glob

path = glob(r'.\dataset\annotations\*.xml')

label_d = {
    'filepath': [],
    'xmin': [],
    'xmax': [],
    'ymin': [],
    'ymax': [],
    'image_path': [],
}

for filename in path:
    tree = xet.parse(filename)
    root = tree.getroot()

    folder_name = root.find('folder').text
    image_name = root.find('filename').text

    object = root.find('object')
    box = object.find('bndbox')

    xmin = int(box.find('xmin').text)
    xmax = int(box.find('xmax').text)
    ymin = int(box.find('ymin').text)
    ymax = int(box.find('ymax').text)

    image_name = os.path.join(r'.\dataset', folder_name, image_name)

    label_d['filepath'].append(filename)
    label_d['xmin'].append(xmin)
    label_d['xmax'].append(xmax)
    label_d['ymin'].append(ymin)
    label_d['ymax'].append(ymax)
    label_d['image_path'].append(image_name)


df = pd.DataFrame(label_d)
df.to_csv('labels.csv', index=False)

print(df.head())