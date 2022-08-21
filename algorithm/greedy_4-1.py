n,k = map(int, input().split())

def firstcase(n):
    return n-1

def secondCase(n,k):
    return n//k

count = 0
while n != 1:
    if n % k == 0:
        n = secondCase(n,k)
    else:
        n = firstcase(n)
    count += 1

print(count)