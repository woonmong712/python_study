# https://codeup.kr/problem.php?id=4036

import math

n = int(input())
m = int(input())

def find_a(n,m):
    return int((n+m)/2)

def find_b(n,m):
    return int((n-m)/2)


print(find_a(n,m))
print(find_b(n,m))