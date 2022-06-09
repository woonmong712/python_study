arr = [list(map(int, input().split())) for _ in range(9)]


def find_maxNum(arr):
    maxNumArr = []
    for i in range(len(arr)):
        maxNumArr.append(max(arr[i]))

    maxNum = max(maxNumArr)
    return maxNum

print(find_maxNum(arr))