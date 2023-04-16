n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
out = []
visited = [False] * n


def dfs(depth):
    # prev변수를 통해 이전에 나온 값과 같은 값이 나오면 제외시켜버리기
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
