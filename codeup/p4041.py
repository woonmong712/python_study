# https://codeup.kr/problem.php?id=4041

number = input()
arr = []

def sum(number):
    total = 0
    for i in number:
        total += int(i)
    return total

def sort_array(number):
    arg = []
    for i in range(len(number)):
        arg.append(number[i])
    arg.reverse()
    if arg[0] == '0':
        del arg[0]
    return arg
        
# 반대로 출력
arr = sort_array(number)
print(''.join(arr))
print(sum(number))
