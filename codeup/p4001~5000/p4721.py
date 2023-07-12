# 투표한 학생 수
N = int(input())

grade = []
for _ in range(N):
    grade.append(list(map(int, input().split())))

""" 해야할 것 정리하기
1. 학생회장 별 점수 배열 필요
2. 점수배열 확인 후, max값, 각 숫자별 값이 필요
3. class 내에 배열값을 받아야 하는 것이 있고, max값과 숫자를 chk할 함수가 필요

"""
class woonmong:
    def __init__(self,num_ary):
        self.num_ary = num_ary

    def maxNum(self,num_ary):
        return max(num_ary)

    def chk_num(num_ary):
        num = num_ary[0]
        return num

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

# def chk_numberCnt():