import cv2

carregaFace = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
carregaOlho = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

imagem = cv2.imread('RostosRF/I3.jpg')
imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
faces = carregaFace.detectMultiScale(imagemCinza, scaleFactor=1.7, minNeighbors=2, minSize=(30, 30))

for(x, y, l, a) in faces:
    imagem = cv2.rectangle(imagem, (x, y), (x + l, y + a), (255, 0, 255), 2)
    localOlho = imagem[y:y + a, x:x + l]
    localOlhoCinza = cv2.cvtColor(localOlho, cv2.COLOR_BGR2GRAY)
    detectado = carregaOlho.detectMultiScale(localOlhoCinza, scaleFactor=1.01, minNeighbors=2, minSize=(30, 30))

    for(ox, oy, ol, oa) in detectado:
        cv2.rectangle(localOlho, (ox, oy), (ox + ol, oy + oa), (0, 0, 255), 2)

cv2.imshow("Detecta Face e os Olhos ", imagem)
cv2.waitKey()