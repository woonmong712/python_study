year = int(input())


Chinese_Zodiac = {4 : 'A', 5 : 'B', 6 : 'C', 7 : 'D', 8 : 'E', 9 : 'F', 10 : 'G', 11 : 'H', 0 : 'I', 1 : 'J', 2 : 'K', 3 : 'L'}
sexagenary_cycle = {4:0, 5:1, 6:2, 7:3, 8:4, 9:5, 0:6, 1:7, 2:8, 3:9}


zodiac_year = int(year%12)
sexagenary_cycle_year = int(year%10)

print(f"{Chinese_Zodiac[zodiac_year]}{sexagenary_cycle[sexagenary_cycle_year]}")
     
