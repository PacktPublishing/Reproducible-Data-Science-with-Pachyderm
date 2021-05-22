import numpy as np
import matplotlib.pyplot as plt
import os
from skimage.io import imread, imsave
from skimage import measure
import logging
logging.basicConfig(level=logging.INFO)
import PIL

def create_contours(photo):
    image = PIL.Image.open(photo, as_gray=True)
    #image = imread(photo, as_gray=True)
    t = os.path.split(photo)[1]
    c = measure.find_contours(image, 0.9)
    fig, ax = plt.subplots()
    ax.imshow(image, vmin=-1, vmax=1, cmap='gray')

    for contour in c:
        ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    plt.savefig(os.path.join("pfs/out", os.path.splitext(t)[0]+'.png'))

for dirpath, dirnames, filenames in os.walk("pfs/data"):
    for f in filenames:
        create_contours(os.path.join(dirpath, f))

