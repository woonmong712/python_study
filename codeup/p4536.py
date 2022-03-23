numArr = []

for i in range(10):
    numArr.append(int(input()))

print(numArr)

def Average_Num(numArr):
    sum = 0
    for i in range(len(numArr)):
        sum += numArr[i]
    return int(sum/len(numArr))

def max_Cnt(numArr):
    dict = {numArr[i]: 0 for i in range(0, len(numArr))}
    for i in range(0,len(numArr)-1):
        # if i == len(numArr)-1:
        #     print(dict)
        if numArr[i] != numArr[i+1]:
            print(f"numArr[i] = {numArr[i]} , numArr[i+1] = {numArr[i+1]}")
            cnt += 1
            dict[numArr[i]] = cnt

    print(dict)


print(max_Cnt(numArr))
