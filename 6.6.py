def cel2fah(cel):
    return (9/5)*cel + 32

for i in range(1,6):
    cel = i*10
    print('섭씨', cel, '도 = 화씨', cel2fah(cel), '도')
