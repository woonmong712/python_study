# 격자판의 세로 : h , 격자판의 가로 : w , 막대의 개수 : n, 각 막대의 길이 : l, 막대를 놓는 방향 (d, 가로 0 세로 1)
# 막대를 놓는 가장 왼쪽, 위쪽의 위치 (x,y)
h,w = map(int,input().split(" "))
n = int(input())

#막대 크기/위치 정보 배열
sticks = []

for i in range(n):
    l,d,x,y = input().split(" ")
    sticks.append([l,d,x,y])

# 0으로 채워진 격자 만들기 (empty)
def made_graph(h,w):
    arg_graph = []
    for i in range(h):
        arg_graph.append([0]*w)
    return arg_graph

# 막대 놓기
def put_the_stick(arg, sticks):
    sticks = list(map(int, sticks))
    x ,y = sticks[2]-1, sticks[3]-1
    n = sticks[0]
    for i in range(0,n):
        if sticks[1] == 0:
            arg[x][y+i] = 1
        elif sticks[1] == 1:
            arg[x+i][y] = 1
        else :
            print("Error")
    return arg

arg = made_graph(h,w)
for i in range(0,n):
    result_arg = put_the_stick(arg, sticks[i])

# 출력하기
for i in range(len(result_arg)):            # 세로 크기
    for j in range(len(result_arg[i])):     # 가로 크기
        print(result_arg[i][j], end=' ')
    print()


