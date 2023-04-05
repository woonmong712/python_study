# 전체 인원 : K, 한 방 인원 : N , 같은 학년, 성별
# 한번 풀고 다음에 구조체를 이용해서 풀어보도록 하기


class student:
    S : int = None
    Y : int = None

K,N = map(int, input().split(" "))
student_class = student()
for student in range(K):
    S,Y = map(int, input().split(" "))
    student.S = 


def chk_sex(student_array):
    girls, boys = [], []
    for i in range(len(student_array)):
        if student_array[i][0] == 0:
            girls.append(student_array[i][1])
        elif student_array[i][0] == 1:
            boys.append(student_array[i][1])
    return girls, boys

def chk_years(student_array):
    years = {1:0,2:0,3:0,4:0,5:0,6:0}
    for i in range(1,len(student_array)+1):
        for j in student_array:
            if i == j:
                years[i] += 1
    return years

def div_room(student_array,N):
    room = 0
    for i in range(1,len(student_array)+1):
        if student_array[i] <= N and student_array[i] != 0:
            room += 1
        elif student_array[i] > N:
            room += 2
    
    return room

div_student_array= chk_sex(student_array)
girls = chk_years(div_student_array[0])
boys = chk_years(div_student_array[1])

print(div_student_array)
print(chk_years(div_student_array[0]))
print(div_room(girls,N)+div_room(boys,N))
