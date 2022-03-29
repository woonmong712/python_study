from collections import Counter

numArr = []

for i in range(10):
    numArr.append(int(input()))

def Average_Num(numArr):
    sum = 0
    for i in range(len(numArr)):
        sum += int(numArr[i])
    return int(sum/len(numArr))

def find_max_num(array):
    # count_num = {}
    # for num in array:
    #     if num not in count_num:
    #         count_num[num] = 0
    #     count_num[num] += 1
    # count_num = sorted(count_num.items(), key=lambda x: x[1], reverse=True)
    # return count_num[0][0]
    counter = Counter(array)
    max_count = -1
    for letter in counter:
        if counter[letter] > max_count:
            max_count = counter[letter]
            max_letter = letter
    return max_letter
    

print(Average_Num(numArr))
print(find_max_num(numArr))
