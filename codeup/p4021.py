# https://codeup.kr/problem.php?id=4021

numbers = list(map(int,input().split()))

def check_odd_num(numbers):
    arr = []
    for i in range(len(numbers)):
        if numbers[i] %2 == 1:
            arr.append(numbers[i])

    return arr

def total_sum(numbers):
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    return sum

numbers = check_odd_num(numbers)
if not numbers:
    print(-1)
else:
    print(total_sum(numbers))

