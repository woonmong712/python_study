participant = int(input())
dice_number_array = [list(map(int, input().split()))
                     for _ in range(participant)]

dice_numDic = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}


def count_number(dict, array):
    for num in array:
        if num in dict:
            dict[num] += 1
    return dict


def initialization_dict(dict):
    dict = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    return dict


priceArray = []
for i in range(participant):
    dice_numDic = count_number(dice_numDic, dice_number_array[i])
    print(dice_numDic)
    # dice_numDic = dict(
    #     {key: value for key, value in dice_numDic.items() if value != 0})
    # reverse_dice_numDic = dict((value, key)
    #                            for (key, value) in dice_numDic.items())
    # print(reverse_dice_numDic)
    # if len(dice_numDic) == 1:
    #     dice_keys = list(dice_numDic.keys())
    #     price = 50000 + dice_keys[0] * 5000
    # elif len(dice_numDic) == 2:
    #     if 3 in
    #     price = 10000 + int(key) * 1000
    # elif len(dice_numDic) == 2 and value == 2
    # print(key)
    # dice_keys = list(dice_numDic.keys())
    # price = 2000 + dice_keys[0] * 500 + dice_keys[1] * 500
    # elif len(dice_numDic) == 3:
    #     print("1")
    # elif value == 1 and len(dice_numDic) == 4:
    #     print("test")
    # priceArray.append(price)
    dice_numDic = initialization_dict(dice_numDic)
# print(priceArray)
