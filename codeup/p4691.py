participant = int(input())
dice_number = []

for cnt in range(participant):
    num = input().split(" ")
    dice_number.append(num)
    
def get_count(num_list):
  count_list = {}
  for i in num_list:
    try: count_list[i] += 1
    except: count_list[i] = 1
  return(count_list)

number_dict = []
total_price = 0
for i in range(participant):
    number_dict.append(get_count(dice_number[i]))

for i in number_dict:
    for key, value in i.items():
        if value == 4:
            total_price = 50000 +  int(key) * 5000
    print(f"total_price = {total_price}")