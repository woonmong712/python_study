# 라운드 수
K = int(input())

# 점수 개수
C = int(input())

# 점수 리스트
grade = []
for i in range(C):
    M,N = map(int,input().split(" "))
    grade.append([M,N])

print(grade)