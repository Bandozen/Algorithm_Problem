n, k = map(int, input().split())
coin = []
for _ in range(n):
    val = int(input())
    coin.append(val)
    
coin = sorted(coin, reverse=True)
# print(coin)
cnt = 0

for i in coin:
    if k != 0:
        cnt += k // i
        k%=i

print(cnt)