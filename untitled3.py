# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 18:46:29 2021

@author: Ryan
"""

import numpy as np 

from scipy.ndimage import variance
from skimage import io
from skimage.color import rgb2gray
from skimage.filters import laplace
from skimage.transform import resize


# Load image
path = "04.jpg"
img = io.imread(path)
#io.imshow(img) 
#io.show()
# Resize image
img = resize(img, (400, 600))

# Grayscale image
img = rgb2gray(img)

# Edge detection
edge_laplace = laplace(img, ksize=3)

result = variance(edge_laplace)
print(result)
# Print output
print(f"Variance: {result}")
print(f"Maximum : {np.amax(edge_laplace)}")

threshold=0.0013

if result > threshold:
	print(" - Not Blurry: ")
elif result <= threshold:
  print(" - Blurry: ")