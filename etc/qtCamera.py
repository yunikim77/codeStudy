
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture

info = QCameraInfo.availableCameras()
infos = QCamera.availableDevices()

print(infos)