# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 12:54:43 2021

@author: Narendran Srinivasan
"""

import cv2
import cv2.aruco as aruco
import numpy as np
import os
def findArucoMarkers(img, markerSize=6, totalMarkers=250, draw=True):

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    key = getattr(aruco, f'DICT_{markerSize}X{markerSize}_{totalMarkers}')
    arucoDict = aruco.Dictionary_get(key)
    arucoParam = aruco.DetectorParameters_create()
    bboxs, ids, rejected = aruco.detectMarkers(imgGray, arucoDict, parameters=arucoParam)

    if draw:
        aruco.drawDetectedMarkers(img, bboxs)
  
    print(ids)

    return [bboxs, ids]

def augumentAruco(bbox, id, img, drawId=True ):   

    image = cv2.putText(img, str(id), (int(bbox[0][0][0]),int(bbox[0][0][1])), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,255),2)
    return image

def main():

    cap = cv2.VideoCapture(0)

    while True:
        success, img = cap.read()
        arucoFound = findArucoMarkers(img)

        if len(arucoFound[0])!=0:
            for bbox, id in zip(arucoFound[0], arucoFound[1]):
                img = augumentAruco(bbox, id, img)

        cv2.imshow("Image",img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()        