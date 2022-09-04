# a : 현재 온도 , b : 목표 온도
a,b= map(int,input().split(" "))

count = 0

degree = abs(b-a)
count = degree // 10 # 10 단위 추가하기
last_degree = degree % 10

if last_degree > 5:
    if last_degree%5 >= 3:
    # 큰 수에서 빼주는 방식으로 진행
        count += 1 # 10단위에서 빼주는 것으로 이해하면 됨
        count += 5 - (last_degree%5)
    elif last_degree%5 < 3:
        count += 1 # 5단위 더해주는 것으로 진행
        count += (last_degree%5) # 숫자대로 더해주면 됨
elif last_degree == 5:
    # 5인 경우에는 온도 1번만 올리기/내리기 하면 됨
    count += 1
elif last_degree < 5:
    if last_degree%5 >= 3:
    # 큰 수에서 빼주는 방식으로 진행
        count += 1
        count += 5 - (last_degree%5)
    elif last_degree%5 < 3:
        count+= (last_degree%5)

print(count)

# 34 > 
# 27 > 3번(+30) 누르고 3번(-1) = 6번
# 27 > 2번(+20) 누르고, 1번(+5) , 2번 (+1) = 7번

# count = abs(b-a)//10

# if abs(b-a)%10 >= 5:
#     count += 1
#     count += abs(b-a)%10 - 5
# else:    
#     count += abs(b-a)%10

# 온도 1을 누르는 숫자를 줄이는 것이 관건, 
# 10 단위는 전부 계산을 하고, 1단위에서 5이상/이하를 따진 뒤, 나누기 2해서 나온 값이 2 이하면 +, 3 이상이면 - 
## 1. 22 40 > 
# 1) 40-22 = 18 > 1번 누르고 (+) 1번 누르고(+5) , 3번 +++ OR 2번 2번
# 2) 22, 40 >> 2번 누르고(+), 2번누르고(-) 4번