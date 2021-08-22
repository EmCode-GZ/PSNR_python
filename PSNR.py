import cv2
import numpy as np
import math


def psnr2(img1, img2):
    mse = np.mean((img1 / 255. - img2 / 255.) ** 2)
    if mse < 1.0e-10:
        return 100
    PIXEL_MAX = 1
    return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))


gt = cv2.imread('cvc-clinic1.png')
img = cv2.imread('cvc-clinic2.png')

print(psnr2(gt, img))
