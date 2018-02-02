import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
import sys

index = []
data1 = []
data2 = []
lineCnt = 0

app = QApplication(sys.argv)

while(True):
    fname = QFileDialog.getOpenFileName(directory="d:\Workspace\Battery\data", filter="*.txt")

    if fname[0] == '':
        print("didn't select file.")
        exit()

    with open(fname[0]) as file:
        for line in file:
            lineCnt += 1
            ld = line.split()
            if ld.__len__() != 3 or ld[0].isdigit() is False:
                continue
            index.append(int(ld[0]))
            data1.append(float(ld[1]))
            data2.append(float(ld[2]))

    plt.figure(figsize=(10,8))
    plt.subplot(211)
    plt.plot(index, data1, label="Ch. Cap.", lw=3, color='green')
    plt.xlabel("Cycle Number")
    plt.ylabel("Capacity")
    plt.legend(loc="lower right")
    plt.grid()
    plt.subplot(212)
    plt.plot(index, data2, label="Ch. Vol.", lw=3, color='red')
    plt.xlabel("Cycle Number")
    plt.ylabel("Voltage")
    plt.legend(loc="lower right")
    #plt.plot(data2[0:1000])
    #plt.ylim(0, 0.033)
    #plt.yticks([0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030])
    plt.grid()
    plt.show()

    index.clear()
    data1.clear()
    data2.clear()
