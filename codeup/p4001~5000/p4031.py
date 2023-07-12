# https://codeup.kr/problem.php?id=4031

numbers = list(map(int,input().split(" ")))

result_sum = 0
even_Array = []
odd_Array = []

for i in range(len(numbers)):
    if numbers[i]%2 == 0:
        even_Array.append(numbers[i])
    else:
        odd_Array.append(numbers[i])

even_Array.sort()
odd_Array.sort()

if not even_Array:
    print(odd_Array[len(odd_Array)-1])
elif not odd_Array:
    print(even_Array[len(even_Array)-1])
else:
    print(even_Array[len(even_Array)-1] + odd_Array[len(odd_Array)-1])
