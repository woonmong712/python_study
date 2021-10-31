k,n = map(int,input().split(" "))
result = 0
result_memo = []


def SuperSum(k,n):
    if k != 0:
        print(f"k : {k} , n: {n}")
        return SuperSum(k-1,n)
    elif k == 0:
        print(f"k=0, n = {n}")
        return n

for i in range(1,n+1):
    print(f"range : {i}")
    result_memo.append(SuperSum(k,i))
    
for i in result_memo:
    result += i

print(result_memo)
print(result)
    # SuperSum(0,n) = n 
    # SuperSum(k,n) = SuperSum(k-1,0)+ ~~ + SuperSum(k-1,n)