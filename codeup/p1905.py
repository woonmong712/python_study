n = int(input())
total_result = 0

def total_sum(n,total_result):
    total_result += n
    if n > 0:
        total_sum(n-1,total_result)


total_result = total_sum(n,total_result)

print(total_result)
