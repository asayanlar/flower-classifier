from pathlib import Path
import os.path
import pandas as pd

flower_img_dir = Path("data_set/flowers")
filepaths = list(flower_img_dir.glob("**/*.jpg"))
labels = list(map(lambda x: os.path.split(os.path.split(x)[0])[1], filepaths))