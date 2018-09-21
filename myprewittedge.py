import cv2
import numpy as np


def myprewittedge(img, t, direction):
    kernelX = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
    kernelY = np.array([[-1,0,1],[-1,0,1],[-1,0,1]])
    # kernelPos45 = np.array([[1,1,0],[1,0,-1],[0,-1,-1]])
    # kernelNeg45 = np.array([[0,1,1],[-1,0,1],[-1,-1,0]])
    if t == None:
        img = cv2.filter2D(img, -1, kernelX) + cv2.filter2D(img, -1, kernelY)
        # + cv2.filter2D(img, -1, kernelPos45) + cv2.filter2D(img, -1, kernelNeg45)
        t = np.mean(img)
        for i in range(10):
            t = get_threshold(img, t)
            print("round:" + str(i) + " new threshold: " + str(t))
        ret, threshImg = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
    else:
        print("task2 threshold: " + str(t))
        img = cv2.filter2D(img, -1, kernelX) + cv2.filter2D(img, -1, kernelY)
        ret, threshImg = cv2.threshold(img, t, 255, cv2.THRESH_BINARY)
    return threshImg

def get_threshold(img, t):
    arr = img.flatten()
    g1 = np.nanmean([tmp if tmp >= t else np.nan for tmp in arr])
    g2 = np.nanmean([tmp if tmp < t else np.nan for tmp in arr])
    newThreshold = 0.5 * (g1 + g2)
    return newThreshold
