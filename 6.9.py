def my_sort(*numbers):
    lst=[]
    for number in numbers:
        lst.append(number)
    lst.sort()
    print('정렬 결과:', lst)

my_sort(45, 3, 4, 56, 5)
my_sort(9, 8, 7, 6,  5, 4, 3)
