#!/usr/bin/env python
# coding: utf-8

# In[139]:


get_ipython().system('pip install easyocr')
get_ipython().system('pip install imutils')


# In[150]:


import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils
import easyocr


# In[151]:


#reading image in openCV using openCV imread
img = cv2.imread('image5.jpeg')
#graycolord the image imported using cvtColor, convert one color code from another, BGR to GRAY
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#displaying imge using matplotlib, it expects image in BGR so we have to change once more t
plt.imshow(cv2.cvtColor(gray,cv2.COLOR_BGR2RGB))


# In[142]:


#displaying this noise reduced and edged image before performing contoring
plt.imshow(cv2.cvtColor(edged,cv2.COLOR_BGR2RGB))


# In[ ]:





# In[ ]:





# In[152]:


#find the coordinates of the contours from the image that is edged 
#we are returning a tree of contours so that we can iterate over different level of contours
#Chain_Approx_Simple returns only the key points of tge contour, if rectangle then 4, if line then 2
contourPoints = cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#grabbing contours
contours = imutils.grab_contours(contourPoints)
# returning top 10 contours in the reverse order 
contours = sorted(contours,key=cv2.contourArea,reverse = True)[:10]


# In[153]:


location = None
for contour in contours:
    approx = cv2.approxPolyDP(contour,10,True)
    if len(approx) == 4:
        location = approx
        break


# In[154]:


location


# In[155]:


#applying masking to isolate the contour we just found (rectangle)
#blank mask, it will be same same as tge size of the grey image, we filled it with 0s
mask = np.zeros(gray.shape, np.uint8)
#display the contours over the mask 
new_image = cv2.drawContours(mask,[location],0,255,-1)
new_image = cv2.bitwise_and(img,img,mask = mask)



 


# In[156]:


plt.imshow(cv2.cvtColor(new_image,cv2.COLOR_BGR2RGB))


# In[157]:


#isolate the contour from the entire mask
(x,y) = np.where(mask == 255)
(x1,y1) = (np.min(x),np.min(y))
(x2,y2) = (np.max(x),np.max(y))
croppedImage= gray[x1:x2+1,y1:y2+1]


# In[158]:


plt.imshow(cv2.cvtColor(croppedImage,cv2.COLOR_BGR2RGB))


# In[ ]:




