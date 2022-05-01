n,k = map(int, input().split(" "))
temperatureArray = list(map(int,input().split()))

# def calculate(array,a,b):
#     div = 0
#     for num in range(a,b):
#         div += temperatureArray[num]
#     return div

# def temperature(temperatureArray, k):
#     arr = []
#     div = 0
#     for num in range(0,len(temperatureArray)):
#         if num+k < len(temperatureArray)+1:
#             div = calculate(temperatureArray,num,num+k)
#             arr.append(div)

#     return arr

def arraySum(a,b,temp):
    total = 0
    for i in range(a,b):
        total += temp[i]
    return total


# arr = temperature(temperatureArray,k)
# print(max(arr))
