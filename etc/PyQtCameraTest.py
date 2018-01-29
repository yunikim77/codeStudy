
from PyQt5.QtMultimedia import QCamera, QCameraInfo

for device in QCamera.availableDevices():       ## device 는 QByteArray type
    print(device.data().decode())               ## device.data() 는 bytes return, device.data().decode() 는 str return

for device in QCameraInfo.availableCameras():   ## device 는 QCameraInfo type
    print(device.deviceName())                  ## device.deviceName() 은 str return

print(QCamera.availableDevices())
print(QCameraInfo.availableCameras())

