import cv2

def readAndSaveImg(filename):
    img = cv2.imread(filename)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('01original.jpg', img)

def displayAndSaveImg(img, imgName):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(imgName, img)