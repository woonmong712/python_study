n, k = map(int, input().split(" "))
temperatureArray = list(map(int, input().split()))


def prefix_sum(temp, n):
    result = 0
    for i in range(n):
        result += temp[i]
    return result


def temp_prefix_sum(temp, n, k):
    arr = []
    total_sum = 0
    for i in range(0, n):
        if i+k <= n:
            result = prefix_sum(temp, i+k) - prefix_sum(temp, i)
            arr.append(result)

    return arr


temp_array_result = temp_prefix_sum(temperatureArray, n, k)
print(max(temp_array_result))
