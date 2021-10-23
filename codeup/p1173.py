import math

hour, min = map(int,input().split())

total_min = hour * 60 + min -30

result_hour = math.floor(total_min/60)
result_min = total_min%60

if result_hour < 0:
    result_hour = 24 + result_hour

print(f"{result_hour} {result_min}")