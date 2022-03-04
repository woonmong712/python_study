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
def put_the_stick(sticks):
    # 1. 기준이 되는 곳을 잡는다.
    # 2. 가로/세로를 확인한다.
    # 3. 2번 조건에 따라서 첫번째 index값만큼 0을 1로 바꿔준다.
    

    return 0

    
print(sticks)
print(made_graph(h,w))



