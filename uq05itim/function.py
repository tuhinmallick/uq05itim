
import numpy as np
from ipywidgets import interact, fixed
from PIL import Image

def imshow(X, resize=None):
"""
 You should create a way to resize an image from an array X.
 The use of widgets is optional but you can take a look to interact.
 We should be able to install this package in Google Colab from your Git
 repo.
 """
    resized_width, resized_height = resize
    image = Image.fromarray(X.astype('uint8'), 'RGB')
    im_resized = image.resize((resized_width, resized_height), Image.ANTIALIAS)
    im_resized.show()
    pass

