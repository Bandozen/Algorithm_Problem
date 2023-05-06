def solution(t, p):
    text = []
    answer = []
    cnt = 0
    for i in range(len(t)):
        text.append(t[i:i+len(p)])
    for i in range(len(text)):
        if len(text[i]) == len(p):
            answer.append(text[i])
    for i in range(len(answer)):
        if int(answer[i]) <= int(p):
            cnt += 1
    return cnt