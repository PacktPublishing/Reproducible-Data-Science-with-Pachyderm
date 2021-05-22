from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import os

def create_histogram(photo):
    image = io.imread(photo)
    t = os.path.split(photo)[1]
    plt.hist(image.ravel(), bins=np.arange(10, 70),  color='blue', alpha=0.5, rwidth=0.7)
    plt.yscale('log')
    plt.margins(x=0.03, y=-0.05)
    plt.xlabel('Intensity')
    plt.ylabel('Count')
    plt.savefig(os.path.join("/pfs/out ", os.path.splitext(t)[0]+'.png'))

for dirpath, dirnames, filenames in os.walk("/pfs/contour"):
    for f in filenames:
        create_histogram(os.path.join(dirpath, f))

