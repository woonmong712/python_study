def tax_calc(money):
    return money*0.35

def pay_tax(tax):
    print("thx for paying", tax)

to_pay = tax_calc(150000000)
pay_tax(to_pay)


def make_juice(fruit):
    return f"{fruit} + 🥛"

def add_ice(juice):
    return f"{juice} + ❄️"

def add_sugar(iced_juice):
    return f"{iced_juice} + 🍬"

juice = make_juice("🍍")
cold_juice = add_ice(juice)
perfect_juice = add_sugar(cold_juice)

print(perfect_juice)