inputStr = input('쉼표로 구분된 정수를 임의의 개수 입력하시오: ')
inputList = inputStr.split(',')

inputIntegers = []
for item in inputList:
    inputIntegers.append(int(item))

print('입력된 정수의 리스트:', inputIntegers)
inputIntegers.sort()

print('정렬된 정수의 리스트: ', end="")
for item in inputIntegers:
    print(item, end =" ")
                           
