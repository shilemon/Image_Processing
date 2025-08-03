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

1. Color Histogram : 
A color histogram represents the color distribution within an image by counting the pixel intensities across different color channels. In this study, we computed the histogram using cv2.calcHist with 8 bins for each of the BGR channels, normalizing the histogram to produce a feature vector. 
  
•	Purpose: To represent the color distribution within an image.  
•	Method: Generates histograms for pixel intensities across the BGR color channels
•	Output: A normalized feature vector representing color distribution.





Code:
<img width="975" height="361" alt="image" src="https://github.com/user-attachments/assets/4a81348e-4a29-489a-86f9-3d432c6d0a41" />
<img width="975" height="326" alt="image" src="https://github.com/user-attachments/assets/a9c47e88-d77a-491f-b418-6dd78d0aed4b" />

Output: 
<img width="975" height="477" alt="image" src="https://github.com/user-attachments/assets/22c9af39-c950-43b6-9013-be4c7cd4d626" />

Edge Detection (Canny)  
 
 
Edge detection identifies the boundaries in an image by highlighting regions of rapid intensity change. We used the Canny edge detector applied to the grayscale image to extract these edges. 
 
➢	Purpose: To detect image boundaries by identifying areas with rapid intensity changes. 
➢	Method: Applies the Canny edge detector to a grayscale image. 
         Output: An edge-detected image that highlights the boundaries

Code:
<img width="975" height="415" alt="image" src="https://github.com/user-attachments/assets/160c572d-5c4c-4b47-80cc-ef3dc30b6801" />

Output:
<img width="975" height="437" alt="image" src="https://github.com/user-attachments/assets/09680ae4-03db-4e92-855a-d124048e5045" />

Contour Detection  
 
Contours are curves that connect continuous points along a boundary with the same color or intensity. We used cv2.findContours to detect contours from the edge-detected image and then drew these contours on the original image. 
  
•	Purpose: To find and highlight object boundaries within an image. 
•	Method: : Detects contours in the edge-detected image and overlays them on the original image
•	Output: An image with contours drawn around the objects

Code :
<img width="975" height="379" alt="image" src="https://github.com/user-attachments/assets/029e2476-8818-46f2-86a8-11bff5c3956c" />
Output:
<img width="975" height="431" alt="image" src="https://github.com/user-attachments/assets/a1d44287-ad4d-4ffb-bf03-9f236571640b" />

SIFT Keypoint Detection  
 
A method for detecting and describing local image features that are invariant to scale, rotation, and illumination changes. 
➢	Purpose: To identify and describe distinctive keypoints in images that are invariant to scale, rotation, and partial invariance to illumination changes, enabling robust object matching and recognition. 
➢	Method: Construct a scale-space by applying Gaussian filters at multiple scales. Detect keypoints as extrema in the Difference of Gaussians (DoG) at multiple scales. Assign orientation to keypoints based on local gradient directions for rotation invariance. Compute a 128-dimensional descriptor for each keypoint based on local image gradients. 
➢	Output: A set of keypoints and their corresponding 128-dimensional feature descriptors, used for image matching, recognition, and other computer vision tasks. 

Code:
<img width="975" height="329" alt="image" src="https://github.com/user-attachments/assets/d8b99fd7-f662-464c-8478-ca55998d4a2b" />

Output:
<img width="975" height="940" alt="image" src="https://github.com/user-attachments/assets/a04f8803-0d18-4d3a-a21f-840a41f26057" />




