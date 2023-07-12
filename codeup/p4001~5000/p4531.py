numArr = []

for i in range(5):
    numArr.append(int(input()))

def Average_Num(numArr):
    sum = 0
    for i in range(len(numArr)):
        sum += numArr[i]
    return int(sum/len(numArr))

def Mid_Num(numArr):
    numArr.sort()
    index = int(len(numArr)/2)
    return numArr[index]

print(Average_Num(numArr))
print(Mid_Num(numArr))