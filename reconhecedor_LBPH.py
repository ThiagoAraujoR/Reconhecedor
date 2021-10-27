import cv2

# Parametros de para o reconhecimento
detectorFace = cv2.CascadeClassifier("haarcascade/haarcascade_frontalface_default.xml")
reconhecedor = cv2.face.LBPHFaceRecognizer_create()
reconhecedor.read("classificadores/classificadorLBPH.yml")
largura, altura = 220, 220
font = cv2.FONT_HERSHEY_TRIPLEX
camera = cv2.VideoCapture(0)

while True:
    conectado, imagem = camera.read()
    # Transformar a imagem para escalas de cinza
    imagemCinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    facesDetectadas = detectorFace.detectMultiScale(imagemCinza,
                                                    scaleFactor=1.5,
                                                    minSize=(30, 30))
    # Posicionamento da imagem e do quadrado de detecção
    for (x, y, l, a) in facesDetectadas:
        imagemFace = cv2.resize(imagemCinza[y:y + a, x:x + l], (largura, altura))
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        id, confianca = reconhecedor.predict(imagemFace)

        if id == 1:
            nome = "Thiago"
        elif id == 2:
            nome = "Luciano"
        cv2.putText(imagem, nome, (x, y + (a + 30)), font, 2, (0, 0, 0))
        cv2.putText(imagem, str(confianca), (x, y + (a + 70)), font, 1, (0, 0, 0))

    cv2.imshow("Para encerrar o reconhecimento pressione a tecla 'Q'", imagem)

    if cv2.waitKey(1) == ord('q'):
        break
camera.release()
cv2.destroyAllWindows()

import main
