n = int(input())

cash = [50000,10000,5000,1000,500,100,50,10]

count = 0

for change in cash:
    if n >= change:
        count += n//change
        n = n%change
        if n%change == 0:
            break

print(count)