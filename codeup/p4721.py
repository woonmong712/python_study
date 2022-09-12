# 투표한 학생 수
N = int(input())

grade = []
for _ in range(N):
    grade.append(list(map(int, input().split())))


def get_count(num_lst):
    total_list = {}
    for i in num_lst:
        for key in range(3):
            total_list[key+1] = i[key]
    return total_list


grade_list = []
for i in grade:
    grade_list.append(get_count(grade))


print(grade_list)
