n, k = map(int, input().split(" "))
temperatureArray = list(map(int, input().split()))

# def temp_prefix_sum(temp,n,k):
#     memo = {0:temp[0]}
#     arr = []
#     for i in range(1,n):
#         memo[i] = memo[i-1] + temp[i]

#     for i in range(0,n):
#         try:
#             arr.append(memo[i+k] - memo[i])
#         except KeyError:
#             break

#     if k == 1:
#         return temp
#     if not arr:
#         arr = [memo[1]]

#     return arr
#temp_array_result = temp_prefix_sum(temperatureArray, n, k)
#print(max(temp_array_result))

def max_num(temp,k):
    max_sum = float('-inf')
    start_index = 0
    curr_sum = 0

    for end, val in enumerate(temp):
        curr_sum += val
        if end - start_index +1 == k:
            max_sum = max(max_sum,curr_sum)
            curr_sum -= temp[start_index]
            start_index += 1
    return max_sum

print(max_num(temperatureArray,k))