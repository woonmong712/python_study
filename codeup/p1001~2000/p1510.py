array_size = int(input())
array_list = [[0 for col in range(array_size)] for row in range(array_size)]

def check_index(index):
   if index < 0:
      index = array_size-1
   elif index > array_size-1:
      index = 0

   return index

index_num = 1
f_num = int(array_size/2)
# 현재 행과 열의 index 주소를 저장
col,row = 0, f_num

# 첫번째 규칙 : 배열을 만든 후, 해당 열의 가운데는 1을 넣어야 한다.
array_list[col][row] = index_num
index_num += 1

# 두번째 규칙 : 현재 array_list의 수가 array_size의 배수인 경우와 배수가 아닌 경우
while index_num != (array_size*array_size)+1:
   if array_list[col][row] % array_size != 0:
      col = check_index(col-1)
      row = check_index(row+1)
      array_list[col][row] = index_num
      index_num += 1
   elif array_list[col][row] % array_size == 0:
      col = check_index(col+1)
      array_list[col][row] = index_num
      index_num += 1


for i in range(len(array_list)):            
    for j in range(len(array_list[i])):     
        print(array_list[i][j], end=' ')
    print()