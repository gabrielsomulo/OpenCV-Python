import cv2

carregaAlgoritmo = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

imagem = cv2.imread('RostosRF/I2.jpg')

imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

faces = carregaAlgoritmo.detectMultiScale(imagemCinza, scaleFactor=1.01, minNeighbors=2, minSize=(30, 30))

print(faces)

for(x, y, l, a) in faces:
    cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 3)

cv2.imshow("Faces ", imagem)
cv2.waitKey()