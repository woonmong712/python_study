from re import L


participant = int(input())
dice_number = []

for cnt in range(participant):
    num = input().split(" ")
    dice_number.append(num)


def dice_rule(dicearr):
    case = 0
    dicearr = set(dicearr)
    if not dicearr:
        case = 1
    else:
        case = 4

    return case


for num in dice_number:
    print(dice_rule(num))
