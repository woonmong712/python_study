from re import M


cnt = int(input())
answer = list(map(int, input().split()))

my_grade = []
grade = 0

for i in range(len(answer)):
    if answer[i] == 1:
        grade = 1
        if i != 0 :
            my_grade.append(grade)
        elif answer[i-1] == 1:
            grade += 1
            my_grade.append(grade)
        elif answer[i-1] == 0:
            grade = 0
            my_grade.append(grade)

print(my_grade)