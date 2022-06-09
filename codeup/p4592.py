# git commit
confetti = int(input())
cnt = 0

arr = []
for num in range(confetti):
    a, b = map(int, input().split(" "))
    arr.append([a, b])

array_list = [[0 for col in range(100)] for row in range(100)]


def change_index(array_list, x, y):
    for i in range(x, x+10):
        for j in range(y, y+10):
            array_list[i][j] = 1
    return array_list


def find_index(array_list, arr):
    for i in range(len(arr)):
        x = arr[i][0]
        y = arr[i][1]
        array_list = change_index(array_list, x, y)

    return array_list


array_list = find_index(array_list, arr)

for i in range(len(array_list)):
    for j in range(len(array_list)):
        cnt += array_list[i][j]

print(cnt)
