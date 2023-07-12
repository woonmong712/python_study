numArr = []

for i in range(9):
    numArr.append(int(input()))

def find_maxNum(numArr):
    max_index = 0
    max_number = numArr[max_index]

    for i in range(len(numArr)):
        if max_number <= numArr[i]:
            max_number = numArr[i]
            max_index = i
    
    return max_number,(max_index+1)

max_number, max_index = find_maxNum(numArr)
print(max_number)
print(max_index)