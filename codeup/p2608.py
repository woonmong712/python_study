# 투표자 수
N = int(input())

# 2차원 배열을 무조건적으로 사용해야 가능할 것으로 보임
n_list = [['O','X'] for _ in range(N)]

# Backtracking , 2개의 투표 결과 중에서 선택이 되면 다음으로 넘어가야 함
def generate_combinations(n_list, row, current_combination, combinations):
    if row == len(n_list):
        combinations.append(current_combination.copy())
        return
    
    for value in n_list[row]:
        current_combination.append(value)
        generate_combinations(n_list, row + 1, current_combination, combinations)
        current_combination.pop()

combinations = []
generate_combinations(n_list, 0, [], combinations)

for combination in combinations:
    print(''.join(combination))
