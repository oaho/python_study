def sort3(a,b,c):
    list = []
    list.append(a)
    list.append(b)
    list.append(c)
    list.sort()
    return list

print('세 수를 입력하세요:')
a=int(input())
b=int(input())
c=int(input())

list=sort3(a, b, c)
print('정렬된 리스트는 다음과 같습니다:', list[0], list[1], list[2])
