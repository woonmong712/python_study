#num_list = list(map(int, input().split()))

#sorted_num_list = sorted(num_list)
#reversed_num_list = list(reversed(sorted_num_list))

#if num_list == sorted_num_list:
#    print("오름차순")
#elif num_list == reversed_num_list:
#   print("내림차순")
#else:
#    print("섞임")


num_list = int(input())
setting_num_list = list(range(num_list))

setting_num_list = list(map(int, input().split()))

sorted_num_list = sorted(setting_num_list)
reversed_num_list = list(reversed(sorted_num_list))

if setting_num_list == sorted_num_list:
    print("오름차순")
elif setting_num_list == reversed_num_list:
   print("내림차순")
else:
    print("섞임")