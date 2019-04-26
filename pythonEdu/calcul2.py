
def myAdd(first, second):
    return first + second

def mySub(first, second):
    return first - second

def myMulti(first, second):
    return first * second

def myDiv(first, second):
    if second == 0:
        return first
    return first / second

def myPow(first, second):
    return first ** second

def myMod(first, second):
    if second == 0:
        return first
    return first % second

def myRemainder(first, second):
    return first // second

def inputNumber(string):
    while True:
        print('{} 숫자를 입력하세요: '.format(string), end='')
        inputNum = input()
        if inputNum.isnumeric():
            break

    return int(inputNum)

possibleOperators = ['+', '-', '*', '/', '**', '//', '%']
def inputOperator():
    while True:
        inputStr = input("\n산술연산자를 입력하세요: ")
        if inputStr in possibleOperators:
            break
        print("이해할 수 없는 연산자입니다. ("+inputStr+") 다시 입력해주세요.")

    return inputStr

def calculate(operator, first, second):
    retValue = 0

    if operator == '+':
        retValue = myAdd(first, second)
    elif operator == '-':
        retValue = mySub(first, second)
    elif operator == '/':
        retValue = myDiv(first, second)
    elif operator == '*':
        retValue = myMulti(first, second)
    elif operator == '**':
        retValue = myPow(first, second)
    elif operator == '%':
        retValue = myMod(first, second)
    elif operator == '//':
        retValue = myRemainder(first, second)

    return retValue


while True:

    operatorStr = inputOperator()
    firstNum    = inputNumber('첫번째')
    secondNum   = inputNumber('두번째')
    resultNum   = calculate(operatorStr, firstNum, secondNum)

    print("\n{} {} {} = {} 입니다!!\n".format(firstNum, operatorStr, secondNum, resultNum))

    if input("계속 하시겠습니까? (Y/N): ").upper() == 'N':
        break
