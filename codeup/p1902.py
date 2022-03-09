n = int(input())
def print_number(n):
    if n != 0:
        print(n)
        print_number(n-1)

print_number(n)