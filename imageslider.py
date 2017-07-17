__author__ = 'awinash'
import cv2
import time
import os
alpha=1
beta=1-alpha
path="/home/awinash/Pictures/slides"
handle=os.chdir(path)
cv2.namedWindow("slider",cv2.WND_PROP_FULLSCREEN)
for root, dirs, files in os.walk(".", topdown=False):
    for i in  range(files.__len__()):
        img1=cv2.imread(files[i],1)
        cv2.imshow("slider",img1)
        if cv2.waitKey(1000) & 0xFF==27:
            break
cv2.destroyAllWindows()