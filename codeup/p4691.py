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
    for key, value in i.items():
      if value == 4:
        total_price = 50000 +  int(key) * 5000
        total_price_array.append(total_price)
        total_price = 0
      elif value == 3:
        total_price = 10000 + int(key) * 1000
        total_price_array.append(total_price)
        total_price = 0
      print(key, value)
    print(f"total_price = {total_price_array}")