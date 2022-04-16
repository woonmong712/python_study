work_time = [list(map(float, input().split())) for _ in range(5)]


def calculate_work_time(work_time):
    day_working_time = []
    for i in range(len(work_time)):
        time = work_time[i][1] - work_time[i][0]
        day_working_time.append(time)
        # 시간 외 근무시간 중 1.0 시간 제외
        day_working_time[i] = day_working_time[i] - 1.0
    return day_working_time


def total_work_time(work_time):
    working_time = calculate_work_time(work_time)
    total_working_time = 0
    for i in range(len(working_time)):
        if working_time[i] <= 0:
            working_time[i] = 0
        elif working_time[i] >= 4.0:
            working_time[i] = 4.0

    for time in working_time:
        total_working_time += time

    return total_working_time


def total_overtimePay(work_time):
    time = total_work_time(work_time)
    overtimePay = ((time/0.5)*5000)
    if time >= 15.0:
        overtimePay -= (overtimePay * 0.05)
    elif time <= 5.0:
        overtimePay += (overtimePay * 0.05)

    return int(overtimePay)


print(total_overtimePay(work_time))
