seat, people = map(int,input().split(" "))

seat_status = [[False] for _ in range(seat)]

def how_to_seat(seat_status,people,count):

    # 종료 조건 : 사람에 따른 좌석 수가 찬 경우
    if cal_seat_status(seat_status) == people:
        print(count)
        count += 1
        return

    # 전체 좌석에 대해 반복적으로 확인 필요
    for i in range(len(seat_status)):
        if not seat_status[i]:
            # 좌석을 앉았으면 True로 변경
            seat_status[i] = True
            count += 1
            print(seat_status)

            how_to_seat(seat_status, people,count)

            seat_status[i] = Fasle
            # count -= 1

# 사람수에 따른 좌석 수 return
def cal_seat_status(seat_status):
    cnt = 0
    for i in range(len(seat_status)):
        if seat_status[i] == True:
            cnt += 1

    return cnt

count = 0
how_to_seat(seat_status, people, count)

print(count)