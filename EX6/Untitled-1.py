import cv2
import matplotlib.pyplot as plt
from google.colab import files
from PIL import Image
import numpy as np
import io

# Choose image file
uploaded = files.upload()

# Read image
img = Image.open(io.BytesIO(next(iter(uploaded.values()))))
img = np.array(img.convert("L"))

# Erosion
kernel = np.ones((3, 3), np.uint8)
eroded = cv2.erode(img, kernel, iterations=1)

# Display images
plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray")
plt.title("Original Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(eroded, cmap="gray")
plt.title("Eroded Image")
plt.axis("off")

plt.show()