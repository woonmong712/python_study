# 피자 1달러 당 최고의 열량인 "최고의 피자"를 구하자

# 토핑 종류
N = int(input())
# A 도우 가격 / B 토핑 가격
A,B = map(int,input().split(" "))
# 도우의 칼로리
C = int(input())
# 3+i : 토핑 칼로리 수
topping = []

if N == 0:
    topping.append(0)
else:
    for i in range(N):
        topping.append(int(input()))

# 열량이 높은 피자를 구하려면 열량이 높은 순으로 정렬해서 먼저 더해줘야 한다.
topping.sort(reverse=True)

# 토핑이 없을 경우
bestPizza_kcal = C
bestPizza_price = A
oneDollar_pizza = int(C/A)

# 열량이 높은 순으로 토핑을 추가한다. (중복 안됨)
for i in topping:
    bestPizza_kcal += i
    bestPizza_price += 


print(topping)