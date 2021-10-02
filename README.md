#ALPR
Automatic License Plate Recognition Using OpenCV and EasyOCR

**KEY STEPS PERFORMED**
1) Read Object image using cv2.
2) Performed the greyscaling using cvtColor.
3) Reduced the noise in the greyscaled image to inhance the edgeing.
4) Used Canny algorithm to get the image with all the edges.
5) Found the Contours Points and sorted top 10 contours in reverse order.
6) Iterated over the countors to find the Polygon with lenght 4 (rectangle), and extracted the location of this contour in the image.
7) Applied masking to isoloate the contour we extracted in last step
8) Extracted the text using OCR


**HERE ARE SOME OF THE RESULTS**


![Screen Shot 2021-10-02 at 2 22 45 AM](https://user-images.githubusercontent.com/44043708/135707902-5e2c0892-e908-418f-bb69-7aad1527be1f.png)

![Screen Shot 2021-10-02 at 2 24 27 AM](https://user-images.githubusercontent.com/44043708/135707895-03b3be93-99a7-4564-bce2-fd5823944df7.png)


