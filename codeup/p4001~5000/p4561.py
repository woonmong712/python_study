numArr = []

for i in range(7):
    numArr.append(int(input()))

def find_odd_num(numArr):
    oddNumArray = []
    for num in numArr:
        if num%2 != 0:
            oddNumArray.append(num)
    return oddNumArray

def total_sum(numArr):
    result = 0
    numArr = find_odd_num(numArr)
    if not numArr:
        result = -1
    else:
        for num in numArr:
            result += num
    return result

def sort_Arr(numArr):
    numArr = find_odd_num(numArr)
    numArr.sort()
    return numArr[0]

print(total_sum(numArr))
if total_sum(numArr) != -1:
    print(sort_Arr(numArr))