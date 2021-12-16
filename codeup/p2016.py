# 입력 : 숫자 길이 입력 , 길이가 n 인 숫자

n = int(input())
number_list = list(map(str,input()))
number_list.reverse()

sort_number_list = []

for i in range(0,n):
    sort_number_list.append(number_list[i])
    if (i+1)%3 == 0 and i != n-1:
        sort_number_list.append(",")

sort_number_list.reverse()

print("".join(sort_number_list))
