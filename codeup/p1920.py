num = int(input())

def get_binary_number(num,lists):
    num1, num2 = divmod(num,2)
    lists.append(num2)
    if num1 == 0 :
        return lists
    else:
        return get_binary_number(num1,lists)

binary_number_array = []
binary_number = get_binary_number(num,binary_number_array)
binary_number_array.reverse()

binary_number_array_str = list(map(str,binary_number))
print("".join(binary_number_array_str))
