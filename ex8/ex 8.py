import cv2
from google.colab import files
from google.colab.patches import cv2_imshow

# Upload image
uploaded = files.upload()
filename = next(iter(uploaded))

# Read image
img = cv2.imread(filename)

# Create kernel
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# Dilate image
dilated = cv2.dilate(img, kernel, iterations=1)

# Display images
print("Original Image")
cv2_imshow(img)

print("Dilated Image")
cv2_imshow(dilated)