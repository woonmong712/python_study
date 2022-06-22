bowl = input()

# ( = 10 , (( = 15 (10+5), () = 10+10 = 20
result = 10
for i in range(1,len(bowl)):
    if bowl[i] == '(' and bowl[i-1] == '(':
        result += 5
    elif bowl[i] == ')' and  bowl[i-1] == ')':
        result += 5
    else:
        result += 10

print(result)