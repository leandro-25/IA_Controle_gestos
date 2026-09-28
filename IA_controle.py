import cv2
import os
import psutil
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from cvzone.HandTrackingModule import HandDetector

CAMERA_INDEX = 0
DETECTION_CON = 0.7


def processoRodando(nomes_processos):
    for proc in psutil.process_iter(["pid", "name"]):
        try:
            if nomes_processos.lower() in proc.info["name"].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    return False


def abrirPaint():
    if processoRodando("mspaint"):
        return
    print("Abrindo o Paint...")
    os.system("start mspaint")


def fecharPaint():
    if not processoRodando("mspaint"):
        return
    print("Fechando o Paint...")
    os.system("taskkill /f /im mspaint.exe")


def ajustarVolume(volume, num_fingers):
    volume.SetMasterVolumeLevelScalar(num_fingers / 5.0, None)
    print(f"Volume {num_fingers * 20}%")


def processarMaos(hands):
    dedosEsquerda = None
    dedosDireita = None

    for hand in hands:
        dedos = detector.fingersUp(hand).count(1)
        if hand["type"] == "Left":
            dedosEsquerda = dedos
        else:
            dedosDireita = dedos

    return dedosEsquerda, dedosDireita


cap = cv2.VideoCapture(CAMERA_INDEX)
detector = HandDetector(detectionCon=DETECTION_CON)

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)

gestoAnteriorEsquerda = None
gestoAnteriorDireita = None

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hands, frame = detector.findHands(frame)

        dedosEsquerda, dedosDireita = processarMaos(hands)

        if dedosEsquerda is None:
            gestoAnteriorEsquerda = None
        elif dedosEsquerda != gestoAnteriorEsquerda:
            gestoAnteriorEsquerda = dedosEsquerda
            if dedosEsquerda == 1:
                abrirPaint()
            elif dedosEsquerda == 4:
                fecharPaint()

        if dedosDireita is None:
            gestoAnteriorDireita = None
        elif dedosDireita != gestoAnteriorDireita:
            gestoAnteriorDireita = dedosDireita
            ajustarVolume(volume, dedosDireita)

        cv2.imshow("Detecção de Gestos", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
    cap.release()
    cv2.destroyAllWindows()
