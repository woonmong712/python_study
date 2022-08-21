size = int(input())
route = list(input().split())

# 시작점
x,y = 1,1

def choiceR_D(num,size):
    num = num+1
    if num > size:
        num = num-1
    return num

def choiceL_U(num):
    num = num-1
    if num == 0:
        num = 1
    return num

for i in route:
    if i == 'R':
        y = choiceR_D(y,size)
    elif i == 'L':
        y = choiceL_U(y)
    elif i == 'U':
        x = choiceL_U(x)
    elif i == 'D':
        x = choiceR_D(x,size)

print(x,y)
