n = int(input())
count = 0

# # 가장 긴 변 A
# for C in range(1,n//2+1):
#     for A in range(0,(n-C)//2):
#         print(A)
#         B = n - (A+C)
#         if (A+B) > C and C >= B and A <= B:
#             count += 1

for a in range(n//2,0,-1):
    if a < (n-a):
        for b in range(1,(n-a//2)):
            if a >= b:
                c = n-a-b
                if c > 0 and b >= c:
                    count += 1
print(count)