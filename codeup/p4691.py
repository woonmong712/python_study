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
total_price_array = []
for i in range(participant):
    number_dict.append(get_count(dice_number[i]))

for i in number_dict:
  if len(i) == 4:
    total_price = int(max(i)) * 100
    total_price_array.append(total_price)
  elif len(i) == 3:
    dice_num = [key for key, value in i.items() if value == 2]
    total_price = 1000 + int(dice_num[0]) * 100
    total_price_array.append(total_price)
  elif len(i) == 2:
    list_of_value = list(i.values())
    if max(list_of_value) == 3:
      dice_num = [key for key, value in i.items() if value == 3]
      total_price = 10000 + int(dice_num[0]) * 1000
      total_price_array.append(total_price)
    if max(list_of_value) == 2:
      dice_num = [key for key, value in i.items() if value == 2]
      total_price = 2000 + int(dice_num[0]) * 500 + int(dice_num[1]) * 500
      total_price_array.append(total_price)
  elif len(i) == 1:
    total_price = 50000 + int(max(i)) * 5000
    total_price_array.append(total_price)
  total_price = 0

print(max(total_price_array))