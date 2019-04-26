
index = 0
expression = input("수식을 입력하세요 : ")

for index in range(len(expression)):
    if not expression[index].isnumeric():
        break

if index >= len(expression):
    exit()

