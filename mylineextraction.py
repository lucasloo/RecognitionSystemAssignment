from skimage.transform import probabilistic_hough_line as phl
import math
def mylineextraction(f):
    lines = phl(f)
    maxLen, p0, p1 = 0, None, None
    for line in lines:
        pa, pb = line
        length = math.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        if length > maxLen:
            maxLen, p0, p1 = length, pa, pb
    return p0, p1