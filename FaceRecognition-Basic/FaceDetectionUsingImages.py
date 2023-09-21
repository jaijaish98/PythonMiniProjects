import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image = cv2.imread(
    '/Users/jayendrans/jaijaish98/Work/Programming/Python/Python Mini '
    'Projects/FaceRecognition-Basic/Images/MultipleFaces/ten-young-people-sitting-together-and-having-fun-H6R3NB.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=50, minSize=(30, 30))
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
cv2.imshow('Face Detection', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
