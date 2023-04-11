def backtracking(N, lst):
    if N == m:
        print(*lst)
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            backtracking(N+1, lst + [data[i]])
            visited[i] = False

n, m = map(int, input().split())
data = list(map(int , input().split()))
data.sort()
visited = [False] * n
backtracking(0, [])