import numpy as np
import cv2

a = cv2.imread('A.pgm')
b = cv2.imread('B.pgm')

diff = a.astype(int) - b.astype(int)
diff_abs = np.abs(diff)
out = diff_abs / diff_abs.max() * 255
cv2.imwrite('out.png', out)
img = cv2.imread('out.png')

hot = cv2.applyColorMap(img, cv2.COLORMAP_HOT)
hsv = cv2.applyColorMap(img, cv2.COLORMAP_HSV)
jet = cv2.applyColorMap(img, cv2.COLORMAP_JET)
turbo = cv2.applyColorMap(img, cv2.COLORMAP_TURBO)

cv2.imwrite("out_hot.png", hot)
cv2.imwrite("out_hsv.png", hsv)
cv2.imwrite("out_jet.png", jet)
cv2.imwrite("out_turbo.png", turbo)