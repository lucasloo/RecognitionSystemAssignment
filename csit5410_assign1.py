import sys
from task1 import *
from myprewittedge import myprewittedge
from mylineextraction import *
import numpy as np
filename = sys.argv[1]
print(filename)
#task1
img = cv2.imread(filename)
displayAndSaveImg(img, "01original.jpg")
#task2
img = cv2.imread(filename)
t = np.amax(img)*0.2
thresh = myprewittedge(img, t, "all")
displayAndSaveImg(thresh,"02binary1.jpg")
#task3
img = cv2.imread(filename)
img = cv2.GaussianBlur(img, (3,3), 0)
thresh = myprewittedge(img, None, "all")
displayAndSaveImg(thresh,"03binary2.jpg")
#task4
thresh = cv2.cvtColor(thresh, cv2.COLOR_BGR2GRAY)
p0, p1 = mylineextraction(thresh)
print(p0, p1)
img = cv2.imread(filename)
cv2.line(img, p0, p1, (255,0,0))
displayAndSaveImg(img, "04longestline.jpg")
#task5