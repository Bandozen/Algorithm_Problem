def backtracking(N, lst):
    if N == m:
        print(*lst)
        return
    
    for i in range(1, n+1):
        if not v[i]:
            v[i] = 1
            backtracking(N + 1, lst + [i])
            v[i] = 0

n, m = map(int, input().split())
v = [0] * (n+1)
backtracking(0, [])