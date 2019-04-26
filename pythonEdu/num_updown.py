import random

cntAns = 0
inputNum = 0

print("1~100 숫자 Up & Down 게임을 시작합니다 !!!")
print("-----------------------------")

setNum = random.randrange(1, 101)

while inputNum != setNum:
    cntAns += 1
    inputNum = int(input("1~100 사이의 숫자를 입력하세요 : "))
    if inputNum > setNum:
        print("Down")
    elif inputNum < setNum:
        print("Up")

print("-----------------------------")
print("{} 번 만에 정답을 맞추셨습니다!!\n".format(cntAns))
