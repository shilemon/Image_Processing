Original Image :
                                      

<img width="521" height="416" alt="image" src="https://github.com/user-attachments/assets/ef0d782a-851b-43d8-90f1-3035296e2133" />

Feature Selection Using Local Variance:   
Using OpenCV and NumPy in Google Colab, I executed a variance-based feature selection technique on an image of Baby Groot. The main concept was to identify areas of the image with a high level of detail or texture, using their local variance as a basis.
Variance measures the intensity variation in image regions:
•	High variance often corresponds to edges, texture, or distinct features.
•	Low variance regions tend to be flat or uniform, contributing less to visual detail.

<img width="975" height="425" alt="image" src="https://github.com/user-attachments/assets/6101c695-6144-462e-b3e7-0efb88ae6ae1" />
<img width="975" height="583" alt="image" src="https://github.com/user-attachments/assets/3457facb-c0cc-42cd-8223-bd7e1daccba6" />
1. Grayscale Conversion
Simplifies image data by removing color, focusing on intensity.
2. Global Variance Computation
Gives an overview of overall pixel variability (5304.38 in our case).
3. Local Variance Map
Using a sliding window (kernel size = 5), we calculated variance in small regions to detect detailed areas.
4. Top 15% Thresholding
We extracted only the top 15% high-variance pixels, assuming these contribute the most important features.
5. Mask Application
We visualized the selected features, showing sharp areas like Groot’s eyes, mouth, and wood texture — all captured effectively.

Output:
<img width="975" height="358" alt="image" src="https://github.com/user-attachments/assets/f9f103c5-3cf1-4259-ad6d-d43923c9ce3f" />

Output Interpretation:
Subplot Title

	Description


Original Grayscale Image

	The base input, converted to grayscale to simplify intensity processing.


Local Variance Map (Heat)

	Highlights areas of high intensity variation. Red areas show strong features and texture.	


Selected Features (High Variance)

	A refined version showing only the most important local features — edges and textures are emphasized.
This method acts as a preprocessing step for tasks like object detection, segmentation, or pattern recognition, helping reduce data size while preserving meaningful structure.

Feature Extraction Techniques:  
In image processing, feature extraction is crucial as it transforms images into forms that are simpler and easier to interpret for analysis. This research examines six primary techniques: color histogram, edge detection, local binary patterns (LBP), contour detection, sift keypoint detection, and Hog features derived from a pre-trained ResNet model. Every technique offers distinctive perspectives, assisting different computer vision tasks

