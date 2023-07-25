# n 개의 계단 오르기, 1~2 만큼 움직일 수 있음

# 계단 수
n = int(input())

# f(n) = f(n-1) + f(n-2)
def Climbing(n):
    if n == 1 or n == 0 :
        return 1
    elif n > 1:
        return Climbing(n-1)+Climbing(n-2)

print(Climbing(n))