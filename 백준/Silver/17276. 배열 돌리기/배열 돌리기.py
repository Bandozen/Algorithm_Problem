def turn(n, d, arr: list):
    n -= 1
    cnt = abs(d) // 45
    minus = False
    if d < 0:
        minus = True
    
    for _ in range(cnt):
        # 양수로 시계방향!
        if not minus:
            pre_list = []
            
            for i in range(n + 1):
                pre_list.append(arr[i][i])
                
            for i in range(n + 1):
                pre_tmp = arr[i][(n + 1) // 2]
                arr[i][(n + 1) // 2] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                pre_tmp = arr[i][n - i]
                arr[i][n - i] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                pre_tmp = arr[(n + 1) // 2][n - i]
                arr[(n + 1) // 2][n - i] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                arr[n - i][n - i] = pre_list[i]
        else:
            pre_list = []
            
            for i in range(n + 1):
                pre_list.append(arr[i][i])
                
            for i in range(n + 1):
                pre_tmp = arr[(n + 1) // 2][i]
                arr[(n + 1) // 2][i] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                pre_tmp = arr[n - i][i]
                arr[n - i][i] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                pre_tmp = arr[n - i][(n + 1) // 2]
                arr[n - i][(n + 1) // 2] = pre_list[i]
                pre_list[i] = pre_tmp
                
            for i in range(n + 1):
                arr[n - i][n - i] = pre_list[i]

t = int(input())

for _ in range(t):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split(' '))) for _ in range(n)]
    turn(n, d, arr)
    
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end = " ")
        print()