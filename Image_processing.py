# Step 1: Upload the image
from google.colab import files
uploaded = files.upload()
# Step 2: Import libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.feature import hog

# Step 3: Load the uploaded image
import io
from PIL import Image

image_name = next(iter(uploaded))  # Get uploaded file name
img = cv2.imread(image_name)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 4: Edge Detection (Canny)
edges = cv2.Canny(img_gray, 100, 200)

# Step 5: Contour Detection
contours, _ = cv2.findContours(img_gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_img = img.copy()
cv2.drawContours(contour_img, contours, -1, (0, 255, 0), 2)
contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

# Step 6: SIFT Keypoint Detection
sift = cv2.SIFT_create()
keypoints, _ = sift.detectAndCompute(img_gray, None)
img_sift = cv2.drawKeypoints(img, keypoints, None)
img_sift = cv2.cvtColor(img_sift, cv2.COLOR_BGR2RGB)

# Step 7: HOG Features Visualization
hog_features, hog_image = hog(img_gray, visualize=True)

# Step 8: Color Histogram
colors = ('r', 'g', 'b')
plt.figure(figsize=(12, 4))
for i, color in enumerate(colors):
    hist = cv2.calcHist([img_rgb], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
plt.title("Color Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.show()

# Step 9: Display all results
plt.figure(figsize=(16, 10))

plt.subplot(2, 3, 1)
plt.title("Original Image")
plt.imshow(img_rgb)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.title("Grayscale Image")
plt.imshow(img_gray, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.title("Edge Detection (Canny)")
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.title("Contours")
plt.imshow(contour_img)
plt.axis('off')

plt.subplot(2, 3, 5)
plt.title("SIFT Keypoints")
plt.imshow(img_sift)
plt.axis('off')

plt.subplot(2, 3, 6)
plt.title("HOG Features")
plt.imshow(hog_image, cmap='gray')
plt.axis('off')

plt.tight_layout()
plt.show()
