year = int(input())

def check_leapYear(year):
    result = " "
    if year%4 == 0 and year%100 !=0:
        result = "yes"
    else:
        if year%400 == 0:
            result = "yes"
        else:
            result = "no"
    return str(result)

print(check_leapYear(year))