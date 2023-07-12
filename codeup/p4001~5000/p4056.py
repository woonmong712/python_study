# input total_salary
total_salary = int(input())

def year_end_tax_adjustment(total_salary):
    EITC = 0
    if total_salary <= 500:
        EITC = total_salary * 0.7
    elif total_salary > 500 and total_salary <= 1500:
        EITC = 350 + (total_salary-500) * 0.4
    elif total_salary > 1500 and total_salary <= 4500:
        EITC = 750 + (total_salary-1500) * 0.15
    elif total_salary > 4500 and total_salary <= 10000:
        EITC = 1200 + (total_salary-4500) * 0.05
    else:
        EITC = 1475 + (total_salary-10000) * 0.02

    return int(EITC)
    
print(year_end_tax_adjustment(total_salary))