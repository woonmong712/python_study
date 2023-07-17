n = int(input())

def fibo(n):
    if n == 1:
        return []
    elif n == 2:
        return [1]

    fib = [1,2]
    for i in range(2,n):
        fib.append(fib[i-1]+fib[i-2])
    return fib

# 초기값 설정 ( n = 1 이면 무조건 답은 2 )
case = [2]
caseIndex = fibo(n)

if n > 2:
    for i in range(n):
        case.append(case[i]+caseIndex[i])
    print(case[n-1])
elif n == 1:
    print(case[0])
elif n == 2:
    print(case[0]+caseIndex[0])

