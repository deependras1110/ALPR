# ALPR
Automatic License Plate Recognition Using OpenCV and EasyOCR

KEY STEPS PERFORMED
1) Read Object image using cv2.
2) Performed the greyscaling using cvtColor.
3) Reduced the noise in the greyscaled image to inhance the edgeing.
4) Used Canny algorithm to get the image with all the edges.
5) Found the Contours Points and sorted top 10 contours in reverse order.
6) Iterated over the countors to find the Polygon with lenght 4 (rectangle), and extracted the location of this contour in the image.
7) Applied masking to isoloate the contour we extracted in last step
8) Extracted the text using OCR
