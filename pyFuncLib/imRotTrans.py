import cv2
import numpy as np
import math

def imRotTrans(img, theta, shift_x, shift_y):
    """
    -> img: imput RGB or Gray_scale images
    -> theta: clock wise rotation angle (radius)
    -> shift_x: shift to right by x
    -> shift_y: shift up by y
    
    <- img_out: the rotated and translated image
    """
    (r, c) = (img.shape[0], img.shape[1])
    img_out = np.zeros((r,c,3))
    for i in range(r): # y
        for j in range(c): # x
            ic = i - r//2 #y
            jc = j - c//2 #x
            x = math.cos(theta) * jc + math.sin(-theta) * ic + c//2
            y = math.sin(theta) * jc + math.cos(theta) * ic + r//2
            if((math.floor(x) + shift_x) >= 0 and (math.ceil(x) + shift_x) < c and (math.floor(y) + shift_y)>= 0 and (math.ceil(y) + shift_y)< r):
                img_out[i, j] = 0.25 * (img[math.ceil(y) - shift_y, math.ceil(x) - shift_x] + img[math.ceil(y) - shift_y, math.floor(x) - shift_x] + img[math.floor(y) - shift_y, math.ceil(x) - shift_x] + img[math.floor(y) - shift_y, math.floor(x) - shift_x])
                # img_out[i, j] = img[round(y), round(x)]

    return img_out
