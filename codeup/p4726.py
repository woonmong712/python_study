n,k = map(int, input().split(" "))
temperatureArray = list(map(int,input().split()))

# # def calculate(array,a,b):
# #     div = 0
# #     for num in range(a,b):
# #         div += temperatureArray[num]
# #     return div
# # def temperature(temperatureArray, k):
# #     arr = []
# #     div = 0
# #     for num in range(0,len(temperatureArray)):
# #         if num+k < len(temperatureArray)+1:
# #             div = calculate(temperatureArray,num,num+k)
# #             arr.append(div)
# #     return arr

def arraySum(num,temp):
    total = 0
    for i in range(num):
        total += temp[i]
    return total

def calculate(n,k,temp):
    arr = []

    if len(temp) >= i+k:
        result = arraySum(i+k,temp) - arraySum(i,temp)
        arr.append(result)
    return 0

arr = arraySum(n,temperatureArray)
def temperature(n,temp):
    if arr(n) != 0:
        return arr(n)
    arr[n]m = arraySum(n+k,temp)-temperature(n,temp)
    
    return arr[n]