# 큰 수의 법칙 (p92)
# 입력 조건 : n (2 <= n <= 1000), m (1 <= m <= 10000), k(1<=k<=10000)

# N : 자연수의 개수, M : 더하는 횟수 , K : 제한 횟수 (반복)
N,M,K = map(int, input().split())
# 현재는 제한이 없게 구현되었으나, 추후 제한이 있도록 수정 필요
N_array = list(map(int, input().split()))
# 계산을 용이하게 하기 위해 배열을 오름차순으로 정렬
reversed_sorted_N_array = list(reversed(sorted(N_array)))

def total_sum(m,k,array):
    count,total = 0,0
    # m 횟수 만큼 더해준다.
    for i in range(m):
        if count != k:
            total += array[0]
            count += 1
        elif count == k:
            total += array[1]
            count = 0

    return total

print(total_sum(M,K,reversed_sorted_N_array))
