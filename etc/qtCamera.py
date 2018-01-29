
from PyQt5.QtMultimedia import QCamera, QCameraInfo

info = QCameraInfo.availableCameras()
infos = QCamera.availableDevices()

print(info)
print(infos)