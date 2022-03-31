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
    max_num = numArr[0]
    for number in numArr:
        for compare_number in number:
            if number == compare_number:
                cnt += 1
                max_num = number
            
    # print(dict)
print(Average_Num(numArr))
print(max_Cnt(numArr))
