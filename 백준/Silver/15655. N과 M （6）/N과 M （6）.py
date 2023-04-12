def check(lst):
    l = len(lst)
    for i in range(l-1):
        for j in range(i + 1, l):
            if lst[i] > lst[j]:
                return False
    return True

def backtracking(N, lst):
    if N == m:
        if check(lst):
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