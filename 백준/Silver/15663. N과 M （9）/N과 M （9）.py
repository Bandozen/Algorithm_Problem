n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
out = []
visited = [False] * n
prev = 0


def dfs(depth):
    prev = 0
    if depth == m:
        print(' '.join(map(str, out)))
        return
    for i in range(n):
        if nums[i] != prev and visited[i] == False:
            out.append(nums[i])
            prev=nums[i]
            visited[i]=True
            dfs(depth + 1)
            out.pop()
            visited[i]=False

dfs(0)