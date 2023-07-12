# https://codeup.kr/problem.php?id=4506

# from math import gcd, lcm

# a,b = map(int, input().split(" "))

# print(gcd(a,b))
# print(lcm(a,b))

a,b = map(int, input().split(" "))

# 최대공약수
def GCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a

# 최소공배수 : 두 수를 곱하고 최대공약수로 나누기
def LCM(a,b):
    return int((a*b)/GCD(a,b))

print(GCD(a,b))
print(LCM(a,b))
