n = int(input())

def total_sum(n):
    print(n)
    n += n
    if n != 0:
        total_sum(n-1)
    return n


print(total_sum(n))
