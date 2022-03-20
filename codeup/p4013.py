num = int(input())

def change_binary_num(num):
    return bin(num)[2:]

def change_octal_num(num):
    return oct(num)[2:]

def change_decimal_num(num):
    decimal_number = hex(num)[2:]
    return decimal_number.upper()


print(f"2 {change_binary_num(num)}")
print(f"8 {change_octal_num(num)}")
print(f"16 {change_decimal_num(num)}")