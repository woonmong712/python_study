B = int(input())
N = int(input())
N_list = list(map(int, input().split()))

def backtracking(B, N_list, visited, path, budget, case):
    if budget > B:
        return
    else:
        #case.append(path.copy())
        case.append(budget)
        
    if len(path) == len(N_list):
        return

    for i in range(len(N_list)):
        if not visited[i]:
            visited[i] = True
            path.append(N_list[i])
            budget += N_list[i]

            backtracking(B, N_list, visited, path, budget, case)

            visited[i] = False
            path.pop()
            budget -= N_list[i]

case = []
backtracking(B, N_list, [False] * N, [], 0, case)
print(max(case))