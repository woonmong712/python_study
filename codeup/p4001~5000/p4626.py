cnt = int(input())
answer = list(map(int, input().split()))

grade_array = []
grade_count = 0
for grade in answer:
    if grade == 1:
        grade_count += 1
        grade_array.append(grade_count)
    elif grade == 0:
        grade_count = 0
        grade_array.append(grade_count)   
    
print(sum(grade_array))