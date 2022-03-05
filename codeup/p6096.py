# 2차원 배열 입력받기 
arr = [list(map(int, input().split())) for _ in range(19)]
n = int(input())
for i in range(n):
    x,y = map(int,input().split(" "))

for i in range(1,20):
    if arr[i][int(y)] == 0:
        arr[i][int(y)] = 1
    else:
        arr[i][int(y)] = 0
