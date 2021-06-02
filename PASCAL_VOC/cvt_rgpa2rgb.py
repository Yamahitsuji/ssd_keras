from PIL import Image
import os

filepath = "./data/Images/"
filenames = os.listdir(filepath)
for filename in filenames:
    img_path = filepath + filename
    org_img = Image.open(img_path)

    if org_img.mode == "RGB":
        continue
    elif org_img.mode == "RGBA":
        rgb_img = org_img.convert("RGB")
        rgb_img.save(img_path)
    else:
        print("unexpected format image:", org_img.mode)
