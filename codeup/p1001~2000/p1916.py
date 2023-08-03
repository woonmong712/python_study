N = int(input())

memo = {0:0,1:1}

def fibo(n,memo):
    if n in memo:
        return memo[n]

    if n <= 1:
        return n
    
    memo[n] = fibo(n-1,memo) + fibo(n-2,memo)
    return memo[n]

print(fibo(N,memo)%10009)