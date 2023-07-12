# 2차원 배열 입력받기 
arr = [list(map(int, input().split())) for _ in range(19)]
n = int(input())


for i in range(n):
    x,y = map(int,input().split(" "))
    for j in range(0,19):
        if arr[j][int(y-1)] == 0:
            arr[j][int(y-1)] = 1
        else:
            arr[j][int(y-1)] = 0
        if arr[int(x-1)][j] == 0:
            arr[int(x-1)][j] = 1
        else:
            arr[int(x-1)][j] = 0

# 출력하기
for i in range(len(arr)):            # 세로 크기
    for j in range(len(arr[i])):     # 가로 크기
        print(arr[i][j], end=' ')
    print()