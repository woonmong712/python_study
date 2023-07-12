# 최대 공약수 구하기
a,b = map(int,input().split(" "))

# 최대공약수
def GCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a

print(GCD(a,b))