n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n
tmp = []

def dfs(start):
    if len(tmp) == m:
        print(*tmp)
        return
    remember = 0
    for i in range(start, n):
        if not visited[i] and remember != nums[i]:
            visited[i] = True
            tmp.append(nums[i])
            remember = nums[i]
            dfs(i+1)
            visited[i] = False
            tmp.pop()
            
dfs(0)