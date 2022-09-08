a=[2, 3, 4, 5, 6]
rev_a=[]
print('a=', a)

for _ in range(len(a)):
    rev_a.append(a.pop())
print('rev_a=',rev_a)

rev_a = a[: :-1]
print('rev_a', rev_a)
