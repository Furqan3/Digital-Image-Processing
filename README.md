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
