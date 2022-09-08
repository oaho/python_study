n_list = [10, 20, 30, 50, 60]
min_n = n_list[0]

for i in n_list:
    if i < min_n:
        min_n=i

print('리스트의 원소들 :', n_list)
print('리스트의 원소들 중 최솟값:', min_n)
