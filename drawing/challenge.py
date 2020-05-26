import cv2
import numpy as np
canvas = np.zeros((255, 255, 3), dtype = 'uint8')
flag = True
for i in range(0, 300, 10):
    flag = not flag
    for j in range(0, 300, 10):
        if flag:
            cv2.rectangle(canvas, (i,j), (i+10, j+10), (0, 0, 255), -1)
        flag = not flag
cv2.circle(canvas, (canvas.shape[1] // 2, canvas.shape[0] //2), 30, (0, 255, 0), -1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)
