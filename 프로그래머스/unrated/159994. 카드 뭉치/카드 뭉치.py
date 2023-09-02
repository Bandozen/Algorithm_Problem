def solution(cards1, cards2, goal):
    c1 = []
    c2 = []
    
    cnt = 0
    for i in cards1:
        if i not in goal:
            cnt += 1
            
    for _ in range(cnt):
        cards1.pop()
        
    cnt = 0
    for i in cards2:
        if i not in goal:
            cnt += 1
            
    for _ in range(cnt):
        cards2.pop()
        
    for i in goal:
        if i in cards1:
            c1.append(i)
        else:
            c2.append(i)
            
    if c1 == cards1 and c2 == cards2:
        return "Yes"
    else:
        return "No"