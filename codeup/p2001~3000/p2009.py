my_coupon_cnt, need_coupon_cnt = input().split(' ')

def change_americano(my_coupon_cnt, need_coupon_cnt):
    tries,coffee = 0,0
    remaining_coupon = int(my_coupon_cnt)
    while int(remaining_coupon) >= int(need_coupon_cnt):
        tries = int(remaining_coupon)/int(need_coupon_cnt)
        coffee += int(tries)
        remaining_coupon = int(int(remaining_coupon)%int(need_coupon_cnt)) + int(tries)
    return coffee
    
print(change_americano(my_coupon_cnt,need_coupon_cnt))
