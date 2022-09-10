from random import randint


def generate_numbers():
    numbers = []

    # 코드를 작성하세요.
    while len(numbers) < 3:
        new_number = randint(0,9)
        if new_number not in numbers:
            numbers.append(new_number)
        
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return numbers

def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    
    new_guess = []
    tries = 1
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        new_number = int(input(f"{tries}번째 숫자를 입력하세요:"))
        if new_number in new_guess:
            print("중복되는 숫자입니다. 다시 입력하세요")
        elif new_number > 9 or new_number < 0:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        else:
            new_guess.append(new_number)
            tries += 1
    
    return new_guess

def get_score(guesses, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in solution:
        if i in guesses:
            if solution.index(i) == guesses.index(i):
                strike_count += 1
            else:
                ball_count += 1

    return strike_count, ball_count


# 여기서부터 게임 시작!
ANSWER = generate_numbers()
strike_count, ball_count = 0,0
tries2 = 0

# 코드를 작성하세요.
while strike_count != 3:
    strike_count, ball_count = get_score(take_guess(),ANSWER)
    print(f"{strike_count}S {ball_count}B")
    tries2 += 1
    
print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries2))
