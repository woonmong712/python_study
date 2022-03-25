numArr = []

for i in range(10):
    numArr.append(input())

def Average_Num(numArr):
    sum = 0
    for i in range(len(numArr)):
        sum += int(numArr[i])
    return int(sum/len(numArr))

def max_Cnt(numArr):
    cnt = 0
    dict = {numArr[i]: 0 for i in range(0, len(numArr))}
    numArr2 = numArr
    for i in range(len(numArr)):
        for j in numArr2:
            cnt += 1
        
    return dict
    # print(dict)
print(Average_Num(numArr))
print(max_Cnt(numArr))
