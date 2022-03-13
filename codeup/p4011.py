id = input()

def check_years(sex,year):
    if sex == '1' or sex == '2':
        sex_year = "19" + year
    elif sex == '3' or sex == '4':
        sex_year = "20" + year
    return sex_year

def divide_id(id):
    year = id[0:2]
    month = id[2:4]
    day = id[4:6]
    sex = id[7]

    return year,month,day,sex

def check_sex(sex):
    is_male = 'F'
    if sex == '1' or sex == '3':
        is_male = 'M'
    elif sex == '2' or sex == '4':
        is_male = 'F'
    return is_male

year,month,day,sex = divide_id(id)
year = check_years(sex,year)
sex = check_sex(sex)

print(f"{year}/{month}/{day} {sex}")