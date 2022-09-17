# 학교의 수
N = int(input())

evy_array = []
# 학생수 and 사과 수
for i in range(N):
    student, apple = map(int,input().split(" "))
    evy_array.append([student,apple])

leave_apple = 0
for i in range(N):
    if evy_array[i][0] > evy_array[i][1]:
        leave_apple += evy_array[i][1]
    else:
        leave_apple += evy_array[i][1] % evy_array[i][0]

print(leave_apple)