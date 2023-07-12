h,m,s = map(int,input().split(" "))
cooking_second = int(input())

def time_calculation(cooking_second):
    s = cooking_second%60
    m = int(cooking_second/60)
    h = int(cooking_second/60/60)

    if m >= 60:
        m = int(m%60)
    if h >= 24:
        h = int(h%24)

    return h,m,s

def changeSecond(h,m,s):
    h = 60 * 60 * h
    m = 60 * m
    s += h+m

    return s

total_time = cooking_second + changeSecond(h,m,s)

total_h, total_m, total_s = time_calculation(total_time)
print(total_h, total_m, total_s)


# tc_h,tc_m,tc_s = time_calculation(cooking_second)

# tc_h += h
# tc_m += m
# tc_s += s

# def change_Time(tc_h,tc_m,tc_s):
#     if tc_s >= 60:
#         tc_s = tc_s%60
#         tc_m += 1

#     if tc_m >= 60:
#         tc_m = tc_m%60
#         tc_h += 1

#     if tc_h >= 24:
#         tc_h = tc_h%24
    
#     return tc_h, tc_m, tc_s


# total_h, total_m, total_s = change_Time(tc_h, tc_m, tc_s)
# print(total_h, total_m, total_s)