sentence = list(input())

def check(sc_array):
    result = []
    for i in sc_array:
        if i.islower() == True:
            result.append(i.upper())
        elif i.isupper() == True:
            result.append(i.lower())
        else:
            result.append(i)
    return result

print(''.join(check(sentence)))