def backtracking(N, lst):
    if N == m:
        print(*lst)
        return
    
    for i in range(1, n+1):
        backtracking(N + 1, lst + [i])

n, m = map(int, input().split())
backtracking(0, [])