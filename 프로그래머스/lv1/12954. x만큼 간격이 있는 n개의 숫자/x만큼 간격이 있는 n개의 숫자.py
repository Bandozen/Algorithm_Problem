def solution(x, n):
    answer = []
    if x == 0:
        return [0] * n
    else:
        for i in range(x, x*n+x, x):
            answer.append(i)
        return answer