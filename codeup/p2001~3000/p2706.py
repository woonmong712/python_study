def find_max_sum(numbers):
    n = len(numbers)
    dp = [0] * (n + 1)

    # 한 자리 수는 그대로 저장
    dp[1] = int(numbers[0])

    for i in range(2, n + 1):
        # 현재 숫자를 1자리 수로 나누는 경우
        dp[i] = max(dp[i], dp[i - 1] + int(numbers[i - 1]))

        # 현재 숫자와 이전 숫자를 2자리 수로 묶는 경우
        if i >= 2:
            dp[i] = max(dp[i], dp[i - 2] + int(numbers[i - 2:i]))

    return dp[n]

# 입력 예시
n = list(str(input()))

result = find_max_sum(n)
print(result)  # 출력 결과: 296
