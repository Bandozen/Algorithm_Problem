def backtracking(N, idx):
    if N == m:
        print(' '.join(map(str, lst)))
        return
    
    for i in range(idx, n+1):
        lst.append(i)
        backtracking(N + 1, i)
        lst.pop()

n, m = map(int, input().split())
lst = []
backtracking(0, 1)