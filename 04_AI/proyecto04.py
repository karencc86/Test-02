import cv2 #acceder a la cámara de mi laptop
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastreador = HandDetector(detectionCon=0.8, maxHands=2) #para detectar las manos

while True: 
    exito, imagen = webcam.read()
    coordenadas, imagen_manos = rastreador.findHands(imagen)
    print(coordenadas)

    cv2.imshow("Proyecto 4 - IA", imagen)

    if cv2.waitKey(1) != -1:
       break

webcam.release()
cv2.destroyAllWindows()

