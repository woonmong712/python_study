a,b = map(int,input().split(" "))
arr = []

def print_oddNum(a,b):
    if a <= b:
        if a%2 != 0:
            arr.append(a)
        a += 1
        print_oddNum(a,b)

print_oddNum(a,b)
print(*arr, sep = ' ')