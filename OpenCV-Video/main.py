# Exemplo 01

import cv2

webCamera = cv2.VideoCapture(0)

while True:
    camera, frame = webCamera.read()

    cv2.imshow('Imagem webCamera', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webCamera.release()
cv2.destroyAllWindows()

