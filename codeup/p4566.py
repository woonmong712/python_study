m = int(input())
n = int(input())

def create_Numlist(m,n):
    numlist = []
    for num in range(m,n+1):
        numlist.append(num)
    return numlist

def is_Prime(m,n):
    prime_array = []
    numlist = create_Numlist(m,n)
    for i in range(2,len(numlist)):
        if numlist[i-2]%i != 0:
            prime_array.append(numlist[i])
    return prime_array

print(create_Numlist(m,n))
print(is_Prime(m,n))