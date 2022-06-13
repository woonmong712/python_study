student = int(input())

vote_grade = []
for i in range(student):
    a,b,c = map(int,input().split(" "))
    vote_grade.append([a,b,c])


print(vote_grade)