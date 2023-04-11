def backtracking(N, lst):
    if N == m:
        print(*lst[1:])
        return
    
    for i in range(lst[-1], n+1):
        backtracking(N + 1, lst + [i])

n, m = map(int, input().split())
backtracking(0, [1])