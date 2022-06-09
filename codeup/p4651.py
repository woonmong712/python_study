arr = [list(map(int, input().split())) for _ in range(3)]

grade = []

def check_arr(arr):
    cnt = 0
    for i in arr:
        if i  == 1:
            cnt += 1
    
    return cnt

for i in range(3):
    print(arr)
    print(check_arr(arr[i]))
    if check_arr(arr[i]) == 4:
        grade.append("E")


print(grade)