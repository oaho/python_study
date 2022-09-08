date = input('주민등록번호 첫 6숫자 형식 입력:')

year = int(date[0] + date[1])

if year >= 50:
    year += 1900
else :
    year += 2000

month = int(date[2]+date[3])
day = int(date[4]+date[5])

print('{y}년 {m}월 {d}일'.format(y=year, m=month, d=day))
