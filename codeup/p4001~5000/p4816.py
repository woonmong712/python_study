# 요리 시간 (T초)
T = int(input())

A,B,C = 300,60,10

if T % 10 == 0:
    print((T//A), ((T%A)//B), ((T%A)% B)//C)
else:
    print(-1)