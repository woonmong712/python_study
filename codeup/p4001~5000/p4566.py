m = int(input())
n = int(input())

def create_Numlist(m,n):
    numlist = []
    for num in range(m,n+1):
        numlist.append(num)
    return numlist

def prime_list(m,n):
    primeList = create_Numlist(m,n)
    max = int(n**0.5)
    for i in range(len(primeList)):
        for j in range(2,max+1):
            if primeList[i] % j == 0 and primeList[i] / j != 1 or primeList[i] == 1:
                primeList[i] = 0
    remove_set = {0}
    primeList = [i for i in primeList if i not in remove_set]
    return primeList

def total_sum(numList):
    total = 0
    for i in range(len(numList)):
        total += numList[i]
    return total

primeList = []
primeList = prime_list(m,n)

print(total_sum(primeList))
print(primeList[0])