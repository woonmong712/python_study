from random import *

NUMBER = 6

def generate_numbers(n):
    num_list = []
    while len(num_list) < n:
        num = randint(1, 45)
        if num not in num_list:
            num_list.append(num)
    #print(num_list)
    return num_list

def draw_winning_numbers():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

def count_matching_numbers(numbers, winning_numbers):
    new_list = []
    for i in winning_numbers:
        if i in numbers:
            new_list.append(i)
    return new_list


def check(numbers,winning_numbers):
    check_list = count_matching_numbers(numbers,winning_numbers)
    winning_price = 0

    if winning_numbers[6] not in check_list:
        if len(check_list) == 6:
            winning_price = 100000000
        elif len(check_list) == 5:
            winning_price = 1000000
        elif len(check_list) == 4:
            winning_price = 50000
        elif len(check_list) == 3:
            winning_price = 5000
    elif winning_numbers[6] in check_list:
        if len(check_list) == 6:
            winning_price = 50000000
        elif len(check_list) == 5:
            winning_price = 50000
        elif len(check_list) == 4:
            winning_price = 5000

    return winning_price
    
#print(f"금액 : {check(generate_numbers(NUMBER),draw_winning_numbers())} 원")
