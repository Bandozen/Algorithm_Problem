n = int(input())
nums = list(map(int, input().split()))
yeonsanja = list(map(int, input().split()))

minV = 1e9
maxV = -1e9

def dfs(d, total, plus, minus, mul, div):
    global minV, maxV
    if d == n:
        maxV = max(total, maxV)
        minV = min(total, minV)
        return
    if plus:
        dfs(d + 1, total + nums[d], plus - 1, minus, mul, div)
    if minus:
        dfs(d + 1, total - nums[d], plus, minus - 1, mul, div)
    if mul:
        dfs(d + 1, total * nums[d], plus, minus, mul - 1, div)
    if div:
        dfs(d + 1, int(total / nums[d]), plus, minus, mul, div - 1)
        

dfs(1, nums[0], yeonsanja[0], yeonsanja[1], yeonsanja[2], yeonsanja[3])
print(maxV)
print(minV)
