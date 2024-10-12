import cv2 as cv
import numpy as np



camera=cv.VideoCapture(0)

while True:
   _, frame=camera.read()

   laplacian=cv.Laplacian(frame,cv.CV_64F)
   laplacian=np.uint8(laplacian)
   cv.imshow("laplacian",laplacian)

   cv.imshow("camera",frame)

   if cv.waitKey(5) ==ord("1"):
      break
camera.release()
cv.destroyAllWindows()