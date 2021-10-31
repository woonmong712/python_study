def SuperSum(k,n):
    sum = 0
    if k != 0:
        for i in range(1,n+1):
            sum += SuperSum(k-1,i)
        return sum
    elif k == 0:
        return n


while True:
    k,n = map(int,input().split(" "))
    




print(SuperSum(k,n))