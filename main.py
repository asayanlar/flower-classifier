from pathlib import Path
import os.path
import pandas as pd

flower_img_dir = Path("data_set/flowers")
filepaths = list(flower_img_dir.glob("**/*.jpg"))
labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], filepaths))

filepaths = pd.Series(filepaths, name='Filepath').astype(str)
labels = pd.Series(labels, name='Label')

# Concatenate filepaths and labels
image_df = pd.concat([filepaths, labels], axis=1)

#Viewing first 5 images
print(image_df.head())

#Viewing last 5 images
print(image_df.tail())