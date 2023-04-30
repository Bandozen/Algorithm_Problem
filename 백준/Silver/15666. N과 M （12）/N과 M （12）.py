n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
tmp = []

def dfs(start):
    if len(tmp) == m:
        print(*tmp)
        return
    remember = 0
    for i in range(start, n):
        if remember != nums[i]:
            tmp.append(nums[i])
            remember = nums[i]
            dfs(i)
            tmp.pop()
            
dfs(0)