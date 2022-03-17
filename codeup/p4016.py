# https://codeup.kr/problem.php?id=4016
num_arr = list(map(int,input().split()))

def GCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a

gcdnum = num_arr[0]
for i in range(len(num_arr)):
    gcdnum = GCD(gcdnum,num_arr[i])


print(gcdnum)
