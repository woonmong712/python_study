student = int(input())
student_grade = list(map(int,input().split()))

sort_student_score = sorted(student_grade)
score_differnce = sort_student_score[len(sort_student_score)-1]-sort_student_score[0]

print(score_differnce)