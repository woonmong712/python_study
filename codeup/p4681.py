unique_number = list(map(int, input().split(" ")))

# number of verifications
NOV = 0

for num in unique_number:
    NOV += num ** 2

print(NOV % 10)
