num = int(input())
num_list = []
lost_num_list = []

for i in range(1,num+1):
    num_list.append(i)

for i in range(0,num-1):
    mycard = int(input())
    lost_num_list.append(mycard)

print(num_list)
print(lost_num_list)

for number in num_list:
    if number not in lost_num_list:
        print(number)

