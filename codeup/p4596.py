arr = [list(map(int, input().split())) for _ in range(9)]
MAXNUM = 0

def find_maxNum(arr):
    maxNumArr = []
    for i in range(len(arr)):
        maxNumArr.append(max(arr[i]))

    maxNum = max(maxNumArr)
    return maxNum

MAXNUM = find_maxNum(arr)
MAXNUM_INDEX =[(i,j) for i in range(9) for j in range(9) if arr[i][j]==MAXNUM]
print(MAXNUM)
print(MAXNUM_INDEX[0][0]+1, MAXNUM_INDEX[0][1] +1)