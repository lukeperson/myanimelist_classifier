# Resizes images to size 224 to make full use of imagenet pretrained weights

import os, sys
from PIL import Image, ImageOps


size = 224,224

path = os.getcwd() + '/A/'

for im_pth in os.listdir(path):
    try:
        im_pth = path + im_pth
        im = Image.open(im_pth)
        im.thumbnail(size, Image.ANTIALIAS)
        im.save(im_pth, "JPEG")
        print("SUCC:",im_pth)
    except:
        print("FAIL:",im_pth)
