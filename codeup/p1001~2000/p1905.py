import sys

sys.setrecursionlimit(10**5)

def total_sum(n):
    if n <= 1:
        return 1
    return total_sum(n-1) + n

print(total_sum(int(input())))