
while True:
    result = 0

    operatorStr = input("산술연산자를 입력하세요: ")
    firstNum = input("첫 숫자를 입력하세요: ")
    secondNum = input("두번째 숫자를 입력하세요: ")

    if operatorStr == '+':
        result = int(firstNum) + int(secondNum)
    elif operatorStr == '-':
        result = int(firstNum) - int(secondNum)
    elif operatorStr == '/':
        result = int(firstNum) / int(secondNum)
    elif operatorStr == '*':
        result = int(firstNum) * int(secondNum)
    elif operatorStr == '**':
        result = int(firstNum) ** int(secondNum)
    elif operatorStr == '%':
        result = int(firstNum) - int(secondNum)
    elif operatorStr == '//':
        result = int(firstNum) - int(secondNum)
    else:
        print("이해할 수 없는 연산자입니다. ("+operatorStr+") 다시 입력해주세요.")
        continue

    print("{} {} {} = {} 입니다!!".format(firstNum, operatorStr, secondNum, result))

    if input("계속 하시겠습니까? (Y/N): ").upper() == 'N':
        break

