# Exemplo 02

import cv2

from cv2.data import haarcascades

webCamera = cv2.VideoCapture(0)

classificadorVideo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

while True:
    camera, frame = webCamera.read()

    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detecta = classificadorVideo.detectMultiScale(cinza)

    for (x, y, w, h) in detecta:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 3)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCamera.release()
cv2.destroyAllWindows()