
class calculator:
    def __init__(self, oper='+', first=0, second=0):
        self.operator = oper
        self.firstName = first
        self.secondName = second

    def setValue(self, oper, first, second):
        self.operator = oper
        self.firstName = first
        self.secondName = second

    def myAdd(self):
        return self.firstName + self.secondName
    
    def mySub(self):
        return self.firstName - self.secondName

    def myMulti(self):
        return self.firstName * self.secondName

    def myDiv(self):
        if self.secondName == 0:
            return self.firstName
        return self.firstName / self.secondName

    def myPow(self):
        return self.firstName ** self.secondName

    def myMod(self):
        if self.secondName == 0:
            return self.firstName
        return self.firstName % self.secondName

    def myRemainder(self):
        return self.firstName // self.secondName

    def calculate(self):
        if self.operator == '+':
            retValue = self.myAdd()
        elif self.operator == '-':
            retValue = self.mySub()
        elif self.operator == '/':
            retValue = self.myDiv()
        elif self.operator == '*':
            retValue = self.myMulti()
        elif self.operator == '**':
            retValue = self.myPow()
        elif self.operator == '%':
            retValue = self.myMod()
        elif self.operator == '//':
            retValue = self.myRemainder()
        else:
            retValue = 0

        return retValue


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

print("1 " + __name__)

if __name__ == '__main__':
    while True:
        operatorStr = inputOperator()
        firstNum    = inputNumber('첫번째')
        secondNum   = inputNumber('두번째')

        cal1 = calculator(operatorStr, firstNum, secondNum)
        resultNum   = cal1.calculate()

        print("\n{} {} {} = {} 입니다!!\n".format(firstNum, operatorStr, secondNum, resultNum))

        if input("계속 하시겠습니까? (Y/N): ").upper() == 'N':
            break
