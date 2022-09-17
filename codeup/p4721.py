# 투표한 학생 수
N = int(input())

grade = []
for _ in range(N):
    grade.append(list(map(int, input().split())))

# print(total_grade)
A,B,C = [],[],[]
# 학생별 점수 ary를 만들어 준다.
for i in range(N):
    A.append(grade[i][0])
    B.append(grade[i][1])
    C.append(grade[i][2])

A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)

maxSum_ary = [sum(A),sum(B),sum(C)]
maxSum = max(maxSum_ary)
cnt = 0
for num in maxSum_ary:
    if maxSum == num:
        cnt += 1