student = int(input())

vote_grade = []
for i in range(student):
    a,b,c = map(int,input().split(" "))
    vote_grade.append([a,b,c])

candidate1 = []
candidate2 = []
candidate3 = []

for i in range(student):
    candidate1.append(vote_grade[i][0])
    candidate2.append(vote_grade[i][1])
    candidate3.append(vote_grade[i][2])

def choseCase(num1,num2,num3):
    case = 0
    


# def CountNumber(vote_grade,number):
#     cnt = 0
#     cnt_array = []
#     for i in range(3):
#         for j in range(len(vote_grade)):
#             if vote_grade[j][i] == number:
#                 cnt += 1
#         cnt_array.append(cnt)
#         cnt = 0
#     return cnt_array

# total_grade = {1:0,2:0,3:0}
# grade = 0
# three_array = []
# for i in range(3):
#     for j in range(student):
#         grade += vote_grade[j][i]
#     total_grade[i+1] = grade
#     grade = 0

# print(total_grade)
# # dict 내 value 가 최대인 값 찾기
# maxNumArray = [k for k,v in total_grade.items() if max(total_grade.values()) == v]

# print(maxNumArray)
# if len(maxNumArray) == 3:
#     threeCount = CountNumber(vote_grade,3)
#     maxNumber = max(threeCount)
#     maxNumber_index = threeCount.index(maxNumber)
#     print(maxNumArray[maxNumber_index], total_grade[maxNumArray[0]])
# elif len(maxNumArray) == 2:
#     print("2")
# else:
#     print(maxNumArray[0], total_grade[maxNumArray[0]])
