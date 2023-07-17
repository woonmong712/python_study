# 2*n 의 n 값 받기
n = int(input())

# 네모 상자를 채우는 공식 : T(i) = T(i-1) +T(i-2)
def fibo(n):
    cnt = 0
    if n == 1:
        cnt = 1
    elif n == 2:
        cnt = 2

    fib = [1,2]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    cnt = fib[n-1]
    return cnt

print(fibo(n))