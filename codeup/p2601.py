N = int(input())

def fibo(n):
    _curr, _next = 0,1
    for _ in range(n):
        _curr, _next = _next , _curr+_next
    return _curr

print(fibo(N))