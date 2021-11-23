num_cnt = int(input())
setting_num_list = list(range(num_cnt))

setting_num_list = list(map(int, input().split()))

sorted_num_list = sorted(setting_num_list)
reversed_num_list = list(reversed(sorted_num_list))

def check_duplicate_values(num_list):
    cnt = 0
    for i in range(0,len(num_list)-1):
        if num_list[i] == num_list[i+1]:
            cnt += 1
    if cnt == len(num_list)-1:
        return True
        
if check_duplicate_values(setting_num_list) == True:
    print("섞임")
else:
    if setting_num_list == sorted_num_list:
        print("오름차순")
    elif setting_num_list == reversed_num_list:
        print("내림차순")
    else:
        print("섞임")
