s = input('5개 수를 입력하세요:').split()
n_list = []

for n in s :
    n_list.append(int(n))

print('합:', sum(n_lit))
print('평균:', sum(n_list)/len(n_list))
print('최댓값:', max(n_list))
print('최솟값:', min(n_list))
