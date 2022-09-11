participant = int(input())
dice_number = []

# case 1. 중복제외한 주사위 수 집합의 길이로 확인
def chk_dupDiceNum(dice_number):
  # 4개의 수가 모두 같은 경우
  if len(set(dice_number)) == 1:
    return 50000 + dice_number[0] * 5000
  # 2개의 수가 모두 같은 경우 (2가지 케이스) 3 3 3 1 , 2 2 3 3
  elif len(set(dice_number)) == 2:
    if dice_number[1] == dice_number[2]:
      return 10000 + dice_number[3] * 1000
    else:
      return 2000 + dice_number[1] * 500 + dice_number[2] * 500
  # 2개의 수만 같은 경우 (ex 1 1 2 3)
  elif len(set(dice_number)) == 3:
    for i in range(len(dice_number)):
      if dice_number[i] == dice_number[i+1]:
        return 1000 + dice_number[i] * 100
  # 모든 수가 다른 경우
  else:
    return dice_number[3] * 100


# 주사위 수 받기 (int - list)
for cnt in range(participant):
    num = sorted(list(map(int, input().split())))
    dice_number.append(chk_dupDiceNum(num))

print(max(dice_number))

# def get_count(num_list):
#   count_list = {}
#   for i in num_list:
#     try: count_list[i] += 1
#     except: count_list[i] = 1
#   return(count_list)

# number_dict = []
# total_price = 0
# total_price_array = []
# for i in range(participant):
#     number_dict.append(get_count(dice_number[i]))

# dice_num = []
# for i in number_dict:
#   if len(i) == 4:
#     total_price = int(max(i)) * 100
#     total_price_array.append(total_price)
#   elif len(i) == 3:
#     dice_num = [key for key, value in i.items() if value == 2]
#     total_price = 1000 + int(dice_num[0]) * 100
#     total_price_array.append(total_price)
#   elif len(i) == 2:
#     list_of_value = list(i.values())
#     if max(list_of_value) == 3:
#       dice_num = [key for key, value in i.items() if value == 3]
#       total_price = 10000 + int(dice_num[0]) * 1000
#       total_price_array.append(total_price)
#     if max(list_of_value) == 2:
#       dice_num = [key for key, value in i.items() if value == 2]
#       total_price = 2000 + int(dice_num[0]) * 500 + int(dice_num[1]) * 500
#       total_price_array.append(total_price)
#   elif len(i) == 1:
#     total_price = 50000 + int(max(i)) * 5000
#     total_price_array.append(total_price)
#   total_price = 0

# print(max(total_price_array))