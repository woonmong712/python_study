student = int(input())

vote_grade = []
for i in range(student):
    a,b,c = map(int,input().split(" "))
    vote_grade.append([a,b,c])

total_grade = {1:0,2:0,3:0}
grade = 0
for i in range(3):
    for j in range(student):
        grade += vote_grade[j][i]
    total_grade[i+1] = grade
    grade = 0

arr = (k for k , v in total_grade.items() if max(total_grade.values) == v)
print(arr)
