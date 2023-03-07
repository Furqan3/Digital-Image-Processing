# Digital-Image-Processing
This Repository includes only my Lab task of the course Digital Image Processing
## Lab 1
## Lab Objective:
To introduce students with python programming language and its packages.

## Lab 2
### Lab Objective:
To introduce students with python programming language and its packages

## Lab 3
### Lab Objective:
The objective of this lab is to understand concept of connected component analysis algorithm and 
apply on different images to count objects.
### Lab Description: 
 #### Connected Component Analysis
Connected Component Analysis or Labelling enables us to detect different objects from a binary 
image. Once different objects have been detected, we can perform a number of operations on them: 
from counting the number of total objects to counting the number of objects that are similar, from 
finding out the biggest object of the bunch to finding out the smallest and from finding out the 
closest pair of objects to finding out the farthest etc. 
Connected Component labelling procedure is as follows:
- Process the image from left to right, top to bottom:
If the next pixel to process is 1
  + If only one from top or left 
 is 1, copy its label.
  + If both top and left are one and have the 
 same label, copy it.
  + If top and left they have different labels
Copy the smaller label
Update the equivalence table.
  + Otherwise, assign a new label.
- Re-label with the smallest of equivalent labels

## Lab 4
### Lab Title: Image Transformation Techniques

### Introduction:
In this lab, we will learn about various image transformation techniques that can be applied to digital images to modify their visual appearance. These techniques include negative transformation, log transformation, pixel value transformation, power law transformation, gray level slicing, and histogram calculation.

### Requirements:

- Python programming language
- OpenCV library for image processing
- Numpy library for array manipulation
### Task 1: Negative Transformation

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Apply negative transformation using the formula: new_pixel_value = 255 - old_pixel_value
- Display the output image using imshow() function
- Save the output image using imwrite() function
### Task 2: Log Transformation

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Apply log transformation using the formula: new_pixel_value = c * log(1 + old_pixel_value)
(where c is a constant and can be adjusted to control the brightness of the output image)
- Display the output image using imshow() function
- Save the output image using imwrite() function
### Task 3: Pixel Value Transformation

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Apply pixel value transformation using the following rules:
- For pixel values less than mean: set output pixel value to 0 or 255 (depending on the task)
- For pixel values greater than mean: set output pixel value to 0 or 255 (depending on the task)
- For pixel values within a range of ±20 mean: set output pixel value to 0 or 255 (depending on the task)
- For all other pixel values: set output pixel value to 0 or 255 (depending on the task)
- Display the output image using imshow() function
- Save the output image using imwrite() function
### Task 4: Power Law Transformation

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Apply power law transformation using the formula: new_pixel_value = c * (old_pixel_value ^ gamma)
(where c is a constant and can be adjusted to control the brightness of the output image)
- Repeat the above step for different values of gamma (0.2, 0.5, 1.2, and 1.8)
- Display the output images using imshow() function
- Save the output images using imwrite() function
### Task 5: Gray Level Slicing

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Apply gray level slicing using the lower limit of 100 and upper limit of 200
- Set all pixel values within this range to 210
- Display the output image using imshow() function
- Save the output image using imwrite() function
### Task 6: Histogram Calculation

- Load the image using OpenCV imread() function
- Convert the image to grayscale using cvtColor() function
- Calculate the histogram of the image by iterating through all pixel values and counting their occurrences
- Display the histogram using Matplotlib library
