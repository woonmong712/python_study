m = int(input())
n = int(input())

perfect_square_root = []
for num in range(m,n+1):
    if (num**(1/2)).is_integer() == True:
        perfect_square_root.append(num)

if not perfect_square_root:
    print("-1")
else:
    print(sum(perfect_square_root))
    print(min(perfect_square_root))
