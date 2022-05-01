h,m = map(int,input().split(" "))
cooking_second = int(input())

def time_calculation(cooking_second):
    m = int(cooking_second%60)
    h = int(cooking_second/60)

    if h >= 24:
        h = int(h%24)

    return h,m

def changeMinute(h,m):
    h = 60 * h
    m = h + m

    return m

total_time = cooking_second + changeMinute(h,m)

total_h, total_m = time_calculation(total_time)
print(total_h, total_m)