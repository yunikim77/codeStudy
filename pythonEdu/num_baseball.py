import random

cntAns = 0
inputNum = ['0', '0', '0']
setNum = ['0', '0', '0']

setNum[0] = str(random.randrange(1, 10, 1))
setNum[1] = setNum[2] = setNum[0]

while setNum[0] == setNum[1]:
    setNum[1] = str(random.randrange(1, 10, 1))
while setNum[0] == setNum[2] or setNum[1] == setNum[2]:
    setNum[2] = str(random.randrange(1, 10, 1))

print("숫자야구 게임을 시작합니다 !!!")
print("-----------------------------")

while True:
    cntAns += 1
    strike = 0
    ball = 0
    inputNum = list(input("숫자 3자리를 입력하세요 : "))

    if len(set(inputNum)) != 3:
        print("서로 다른 3자리 숫자를 입력하세요!!")
        continue

    cntCompare = 0
    while cntCompare < 3:
        if inputNum[cntCompare] in setNum:
            if inputNum[cntCompare] == setNum[cntCompare]:
                strike += 1
            else:
                ball += 1
        cntCompare += 1

    if strike == 3:
        break
    else:
        print("{} Strike, {} Ball 입니다!".format(strike, ball))

print("-----------------------------")
print("{} 번 만에 정답을 맞추셨습니다!!\n".format(cntAns))
