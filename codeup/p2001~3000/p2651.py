seat, people = map(int, input().split(" "))

seat_status = [False for _ in range(seat)]

def how_to_seat(seat_status, people, count, start_index):

    if cal_seat_status(seat_status) == people:
        count += 1
        return count

    for i in range(start_index, len(seat_status)):
        if not seat_status[i]:
            seat_status[i] = True

            count = how_to_seat(seat_status, people, count, i + 1)

            seat_status[i] = False

    return count

def cal_seat_status(seat_status):
    return sum(seat_status)

count = 0

if len(seat_status) == people:
    count = 1
else:
    count = how_to_seat(seat_status, people, count, 0)

print(count)
