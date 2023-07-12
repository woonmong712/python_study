superSum_memo = {}

def SuperSum(k,n):
    key = f"{k},{n}"
    if k == 0:
        superSum_memo[key] = n
        return n
    if not key in superSum_memo:
        sum = 0
        for i in range(1,n+1):
            sum += SuperSum(k-1,i)
        superSum_memo[key] = sum
        return sum
    else:
        return superSum_memo[key]

number_list = []
while True:
    try:
        k,n = map(int,input().split(" "))
        number_list.append([k,n])
    except:
        break

for i in range(0,len(number_list)):
    print(SuperSum(number_list[i][0],number_list[i][1]))