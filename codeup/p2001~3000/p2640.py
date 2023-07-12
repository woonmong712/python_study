n, k = map(int, input().split())

# 분할 정복을 통한 n의 k승을 구함
def reculsive_power(n,k):
    if k == 1:
        return n
    elif k % 2 == 0:
        _curr = reculsive_power(n, k/2)
        result = _curr * _curr
    elif k % 2 == 1:
        _curr = reculsive_power(n, (k-1)/2)
        result = _curr * _curr * n
    # 많은 데이터를 할당하게 되어 return 값 자체에서 나머지값을 구하도록 변경 
    return result%1000000007

print(reculsive_power(n, k))

