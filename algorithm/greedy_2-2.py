# N : 자연수의 개수, M : 더하는 횟수 , K : 제한 횟수 (반복)
N,M,K = map(int, input().split())
N_array = list(map(int, input().split()))
N_array.sort()

first = N_array[N-1]
second = N_array[N-2]

count = int(M/(K+1))* K
count += M % (K+1)

result = 0
result += (count) * first
result += (M-count) * second
print(result)


