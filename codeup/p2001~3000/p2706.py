def find_max_sum(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)

    dp[1] = int(numbers[0])
    
    # 1의 자리로 나누는 경우와 2의자리로 나누는 경우의 max값을 찾아가도록 구현
    for i in range(2, n + 1):
        dp[i] = max(dp[i - 1] + int(numbers[i - 1]), dp[i - 2] + int(''.join(numbers[i - 2:i]))) # 변환 시 오류가 나서 합쳐서 변환하는 것으로 변경

    return dp[n]

# 입력 예시
numbers = list(input())

result = find_max_sum(numbers)
print(result)
