from imutils import imutils
import cv2

image = cv2.imread("pp.png")
translated = imutils.translate(image, 10, 50)
cv2.imshow("Original", image)
cv2.imshow("translated", translated)
cv2.waitKey(0)
