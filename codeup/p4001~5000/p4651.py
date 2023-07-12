arr = [list(map(int, input().split())) for _ in range(3)]

grade = []

def check_arr(arr):
    zero_cnt = 0
    one_cnt = 0
    for i in arr:
        if i  == 1:
            one_cnt += 1
        if i == 0:
            zero_cnt += 1
    
    return one_cnt, zero_cnt

for i in range(3):
    ONE , ZERO = check_arr(arr[i])
    if ONE == 4 and ZERO == 0:
        grade.append("E")
    elif ONE == 3 and ZERO == 1:
        grade.append("A")
    elif ONE == 2 and ZERO == 2:
        grade.append("B")
    elif ONE == 1 and ZERO == 3:
        grade.append("C")
    elif ONE == 0 and ZERO == 4:
        grade.append("D")

for i in range(len(grade)):    
    print(grade[i])