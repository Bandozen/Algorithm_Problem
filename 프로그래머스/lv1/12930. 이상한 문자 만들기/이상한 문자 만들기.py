def solution(s):
    answer = ''
    new_s = s.split(' ')
    for i in new_s:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer += ' '
    return answer[0:-1]