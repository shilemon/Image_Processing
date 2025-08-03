
# 🌱 Feature Extraction on Baby Groot using OpenCV & NumPy

This project demonstrates various **feature extraction techniques** on an image of **Baby Groot**, implemented using **OpenCV** and **NumPy** in **Google Colab**. The goal is to detect and visualize meaningful features like textures, edges, contours, and keypoints — which are essential in tasks like object detection, segmentation, and pattern recognition.

---

## 🖼️ Original Image
![Original Image](https://github.com/user-attachments/assets/ef0d782a-851b-43d8-90f1-3035296e2133)

---

## 🔍 Feature Selection Using Local Variance

Local variance identifies areas in the image with high detail or texture, helping reduce data size while preserving important visual information.

### 📌 Steps:
1. **Grayscale Conversion**  
   Simplifies data by removing color, focusing on intensity.
2. **Global Variance Computation**  
   Measures overall intensity variation (e.g. 5304.38).
3. **Local Variance Map**  
   Uses a 5×5 sliding window to compute local variance.
4. **Top 15% Thresholding**  
   Highlights only the highest 15% variance pixels.
5. **Mask Application**  
   Visualizes high-detail areas like Groot’s eyes and texture.

### 🔥 Outputs:
| Subplot                    | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| Grayscale Image            | Base image converted to grayscale                                           |
| Local Variance Map         | Heatmap showing areas of high variance (texture/edges)                     |
| Selected High-Variance Features | Shows only the strongest visual features                             |

![Variance Heatmap](https://github.com/user-attachments/assets/6101c695-6144-462e-b3e7-0efb88ae6ae1)  
![Variance Mask](https://github.com/user-attachments/assets/3457facb-c0cc-42cd-8223-bd7e1daccba6)  
![Final Output](https://github.com/user-attachments/assets/f9f103c5-3cf1-4259-ad6d-d43923c9ce3f)

---

## 🧪 Feature Extraction Techniques

Each method provides a different perspective and utility depending on the computer vision task:

---

### 🎨 1. Color Histogram

A histogram of pixel intensity for each BGR color channel, normalized to a feature vector.

- **Purpose:** Represents color distribution.
- **Method:** `cv2.calcHist()` with 8 bins per channel.
- **Output:** A normalized histogram feature vector.

#### 📸 Output:
![Color Histogram](https://github.com/user-attachments/assets/22c9af39-c950-43b6-9013-be4c7cd4d626)

---

### ✂️ 2. Edge Detection (Canny)

Highlights sharp changes in intensity to find edges/boundaries.

- **Purpose:** Identify edges.
- **Method:** Canny edge detector on grayscale image.
- **Output:** Edge-detected image.

#### 📸 Output:
![Edge Detection](https://github.com/user-attachments/assets/09680ae4-03db-4e92-855a-d124048e5045)

---

### 🔲 3. Contour Detection

Detects continuous boundary points and draws them on the image.

- **Purpose:** Highlight object boundaries.
- **Method:** `cv2.findContours()` on edge-detected image.
- **Output:** Image with drawn contours.

#### 📸 Output:
![Contours](https://github.com/user-attachments/assets/a1d44287-ad4d-4ffb-bf03-9f236571640b)

---

### 📌 4. SIFT Keypoint Detection

A robust feature extractor for object matching and recognition.

- **Purpose:** Detect and describe scale & rotation-invariant features.
- **Method:** 
  - Create Gaussian scale space.
  - Detect keypoints from DoG.
  - Assign orientation and compute 128-dimension descriptors.
- **Output:** Keypoints and descriptors.

#### 📸 Output:
![SIFT Keypoints](https://github.com/user-attachments/assets/a04f8803-0d18-4d3a-a21f-840a41f26057)

---

### 📊 5. HOG Features

We utilized the Histogram of Oriented Gradients (HOG) method to extract features from the image. This approach captures texture and structure information by analyzing the distribution of gradient directions in localized regions of the image.

- **Purpose:** Extract low-level features representing shape/texture for tasks like object detection.
- **Method:** Utilizes a pre-trained ResNet-50 model to extract features after image preprocessing.
- **Output:** Feature vector encoding gradient-based texture and structure information.

#### 📸 Output:
![HOG Output](https://github.com/user-attachments/assets/f33368c1-25e3-43d4-ad4d-8e8739009832)

---

## 🤖 Potential Applications

These extracted features are vital for:
- Object Detection
- Image Matching
- Pattern Recognition
- Scene Understanding
- Image Compression

---

## 📂 Tools & Libraries Used
- **Google Colab** (runtime environment)
- **OpenCV (cv2)** – image processing
- **NumPy** – numerical computation
- **Matplotlib** – plotting
- **Python 3.x**

---

## 📝 Author
**👨‍💻 EMON SHIL**  

---

## 📌 Note
Make sure to enable GPU/CPU acceleration on Google Colab for faster computation.
