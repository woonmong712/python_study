student = int(input())

grade_board = []
for i in range(student):
    nation,student_number,grade = map(int,input().split(" "))
    grade_board.append([nation,student_number,grade])

reversed_grade_board = sorted(grade_board,reverse=True, key=lambda grade_board : grade_board[2])
nationCount = []
for i in range(student):
    nationCount.append(grade_board[i][0])
nationCount = set(nationCount)
nationCount_dict = {int : 0 for int in nationCount}

total_score = []
for i in range(student):
    if len(total_score) < 3 :
        if reversed_grade_board[i][0] in nationCount_dict:
            nationCount_dict[reversed_grade_board[i][0]] += 1
        if nationCount_dict[reversed_grade_board[i][0]] <= 2:
            total_score.append(reversed_grade_board[i])

for i in range(len(total_score)):
    print(total_score[i][0], total_score[i][1])

