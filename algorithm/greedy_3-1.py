n,m = map(int,input().split())

# 행의 수대로 배열 크기 지정
numbers = [list(map(int, input().split())) for _ in range(n)]

def findMinNum(array):
    MinNum = min(array)
    return MinNum

MinNumbers = []
for i in range(n):
    MinNumbers.append(findMinNum(numbers[i]))

print(max(MinNumbers))