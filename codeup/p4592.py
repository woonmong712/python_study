confetti = int(input())

arr = []
for num in range(confetti):
    a,b = map(int,input().split(" "))
    arr.append([a,b])

array_list = [[0 for col in range(100)] for row in range(100)]

def change_index(array_list,x,y):
    array_list[x][y] = 1
    return array_list

def find_index(array_list,arr):
    for i in range(arr[])


for i in range(len(arr)):
    array_list = change_index(array_list,arr)
    
# print(arr[0][0])
# print(array_list)

for i in array_list :
    for j in i:
        print(j,end=" ")
    print()
    