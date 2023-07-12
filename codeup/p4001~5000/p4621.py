number, order = map(int,input().split(" "))

arr = []
for i in range(1,number+1):
    if number%i == 0:
        arr.append(int(number/i))

arr2 = []
for x in arr:
    if x not in arr2:
        arr2.append(x)
arr2 = sorted(arr2)

if len(arr2) < order:
    print("0")
else:
    print(arr2[order-1])