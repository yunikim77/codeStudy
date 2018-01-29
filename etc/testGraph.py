import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
import sys

index1 = []
index2 = []
data1 = []
data2 = []
lineCnt = 0

app = QApplication(sys.argv)
fname = QFileDialog.getOpenFileName(filter="*.txt")

if fname[0] == '':
    print("didn't select file.")
    exit()

with open(fname[0]) as file:
    for line in file:
        lineCnt += 1
        ld = line.split()
        index1.append(int(ld[0]))
        index2.append(int(ld[1]))
        data1.append(float(ld[2]))
        data2.append(float(ld[3]))

plt.figure(figsize=(8,6))
plt.plot(index1[2:1004], data1[2:1004], label="Ch. Cap.", lw=5)
plt.plot(index2[2:1004], data2[2:1004], label="Dis. Cap.", lw=5)
plt.xlabel("Cycle Number")
plt.ylabel("Capacity")
plt.legend(loc="lower right")
#plt.plot(data2[0:1000])
plt.ylim(0, 0.033)
#plt.yticks([0, 0.005, 0.010, 0.015, 0.020, 0.025, 0.030])
plt.grid()
plt.show()