def mean3(a, b, c):
    return (a+b+c)/3
def max3(a,b,c):
    max=a
    if b>c:
        if max>b:
            return max
        else:
            return b
    else :
        if max>c:
            return max
        else:
            return c
def min3(a,b,c):
    min1=a
    if b>c:
        min2=c
    else :
        min2=b

    if min1>min2:
        return min2
    else :
        return min1

a, b, c = input('세 수를 입력하시오 : ').split()
a, b, c = int(a), int(b), int(c)
print(a, ",", b, ",", c, "의 평균값은", mean3(a,b,c))
      
print(a, ",", b, ",", c, "의 최댓값값은", max3(a,b,c))
print(a, ",", b, ",", c, "의 평균값은", min3(a,b,c))
