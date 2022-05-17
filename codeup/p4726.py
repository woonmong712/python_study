n,k = map(int, input().split(" "))
temperatureArray = list(map(int,input().split()))

def prefix_sum(temp,n):
    # arr = []
    result = 0
    for i in range(n):
        result += temp[i]
        # arr.append(result)
    return result

def calculate(temp,n,k):
    total_sum = 0
    arr = []
    for i in range(n):
        total_sum += temp[i] + temp[i-k]
        arr.append(total_sum)
    return arr

# arr = []
# for i in range(0,10,2):
#     print(i,i+k)
#     arr.append(calculate(temperatureArray,i,i+k))
#     print(arr)
# print(arr)

print(calculate(temperatureArray,10,2))