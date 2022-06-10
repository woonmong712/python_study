participant = int(input())
dice_number_array = [list(map(int, input().split()))
                     for _ in range(participant)]

print(set(dice_number_array[0]))

# def dice_num_check(dice_number):
