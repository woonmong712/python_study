from random import *

NUMBER = 6

def generate_numbers(n):
    num_list = []
    while len(num_list) < n:
        num = randint(1, 45)
        if num not in num_list:
            num_list.append(num)
    return num_list

def draw_winning_numbers():
    num_list = generate_numbers(7)
    sorted_num_list = sorted(num_list)
    sorted_num_list.append(randint(1,45))
    return sorted_num_list

def count_matching_numbers(numbers, winning_numbers):
    new_list = []
    for i in winning_numbers:
        if i in numbers:
            new_list.append(i)
    return new_list

def check(numbers,winning_numbers):
    check_list = count_matching_numbers(numbers,winning_numbers)
    winning_price = 0
    if len(check_list) == 6:
        if winning_numbers[6] in check_list:
            winning_price = 50000000
        else:
            winning_price = 100000000
    elif len(check_list) == 5:
        winning_price = 1000000
    elif len(check_list) == 4:
        winning_price = 50000
    elif len(check_list) == 3:
        winning_price = 5000
    return winning_price
    
print(f"금액 : {check(generate_numbers(NUMBER),draw_winning_numbers())} 원")