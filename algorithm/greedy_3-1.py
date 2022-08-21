from re import L


n,m = map(int,input().split())
result = 0
# 행의 수대로 배열 크기 지정
# numbers = [list(map(int, input().split())) for _ in range(n)]

# def findMinNum(array):
#     MinNum = min(array)
#     return MinNum

# MinNumbers = []
# for i in range(n):
#     MinNumbers.append(findMinNum(numbers[i]))

for i in range(n):
    data = list(map(int,input().split()))
    min_value = min(data)
    result = max(result,min_value)

# print(max(MinNumbers))
print(result)
