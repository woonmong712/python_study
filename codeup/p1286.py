numbers = []

for i in range(5):
    number = int(input())
    if number < -1000000 or number > 1000000:
        break
    numbers.append(number)

def min_num(numbers,min):
    for i in numbers:
        if min > i:
            min = i
    return min

def max_num(numbers,max):
    for i in numbers:
        if max < i:
            max = i
    return max

print(max_num(numbers,numbers[0]))
print(min_num(numbers,numbers[0]))