# 사탕 고르기, 1행 선택 시 1행 선택 불가
n = int(input())
candyList=[list(map(int, input().split())) for _ in range(n)]
print(candyList)

def select_candy(n,selected,row,select_row,candyList,selected_candy,maxCandy):

    if len(selected_candy) == len(candyList):
        select_row = j
        maxCandy.append(sum(selected_candy))
        return
    
    for i in range(row,n):
        for j in range(n-1):
            if not selected[i][j]:
                selected[i][j] = True
                selected_candy.append(candyList[i][j])
                print(selected_candy)

            select_candy(n,selected,i+1,candyList,selected_candy,maxCandy)

            selected[i][j] = False
            selected_candy.pop()

maxCandy = []
selected= [[False] * 2 for _ in range(n)]
select_candy(n,selected,0,0,candyList,[],maxCandy)
print(maxCandy)
