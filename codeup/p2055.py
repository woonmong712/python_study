import math

a,b = map(int,input().split(" "))

def get_divisor(number):
    num = 0
    num = math.sqrt(number)
    numbers = []
    for i in range(1,int(num)+1):
        if number % i == 0:
            numbers.append(i)
            numbers.append(number//i)
    return numbers

def delete_duplication(a,b):
    result = []
    result = get_divisor(a) + get_divisor(b)
    result = list(set(result))
    result.sort()       
    return result
    
temp = delete_duplication(a,b)
print(' '.join(map(str,temp)))