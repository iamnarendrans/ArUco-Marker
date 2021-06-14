# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:33:16 2021

@author: Narendran Srinivasan
"""

import numpy as np
import cv2
import cv2.aruco as aruco

#Select a Pre defined dictionary and create a dictionary object
#dictionary is composed of 250 markers each of which is 6*6 bits in size
aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
img = np.random.random((200,200))

'''
List of parameters in a function
1.)Dictionary Object
2.)ID of the marker
3.)200 - size of the output marker range
4.)Output image
5.)Optional - size of the marker black border
'''
img = aruco.drawMarker(aruco_dict,23,200,img,1)
cv2.imshow("img",img)

#cv2.imwrite("filename.jpg",img)

cv2.waitKey(0)
cv2.destroyAllWindows