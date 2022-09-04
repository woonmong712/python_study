price = []
for i in range(5):
    price.append(int(input()))

pasta = price[:3]
drink = price[3:]

total_price = (min(pasta) + min(drink)) + ((min(pasta)+min(drink))*0.1)

print(total_price)