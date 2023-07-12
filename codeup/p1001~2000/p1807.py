min_range, max_range = map(int,input().split(" "))

def odd(num):
    result = (num * 3) + 1
    return int(result)

def even(num):
    result = num/2
    return int(result)

collatz_num = {}

for i in range(min_range, max_range+1):
    number, length = i,1
    while number != 1:
        if number % 2 == 0:
            number = even(number)
            length += 1
        else:
            number = odd(number)
            length += 1
    collatz_num[i] = length

max_key = max(collatz_num, key=collatz_num.get)
print(f"{max_key} {collatz_num[max_key]}")