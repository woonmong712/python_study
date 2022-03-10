a,b = map(int,input().split(" "))

def print_oddNum(a,b):
    if a%2 != 0 and a <= b:
        print(a)
        a += 1
        print_oddNum(a,b)
    elif a%2 == 0 and a <= b:
        a += 1
        print_oddNum(a,b)

print_oddNum(a,b)