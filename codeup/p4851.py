# 라운드 수
K = int(input())

# 점수 개수
C = int(input())

# 점수 리스트
grade = []
for i in range(C):
    M,N = map(int,input().split(" "))
    grade.append([M,N])

# 나올 수 있는 점수인 경우에는 1, 나올 수 없는 경우에는 0
# 영희의 점수는 grade[0], 동수의 점수는 grade[1]

def chk_grade(grade,K):

    remain_round = K - max(grade)
    gap = abs(grade[0] - grade[1])

    # 영희와 동수의 점수가 같은 경우는 무조건 나올 수 있는 case
    if grade[0] == grade[1]:
        return 1
    # 영희의 점수가 더 높은 경우 (영희의 순서가 선)
    elif grade[0] > grade[1]:
        if (gap - remain_round) <= 2:
            return 1
        else:
            return 0
    # 동수의 점수가 더 높은 경우
    else:
        if (gap - remain_round) <= 1:
            return 1
        else:
            return 0
result_ary = []
for i in range(C):
    result_ary.append(chk_grade(grade[i],K))

for i in range(C):
    print(result_ary[i])
