n = int(input())

def count_block_patterns(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 1000

    return dp[n]

result = count_block_patterns(n)
print(result)
