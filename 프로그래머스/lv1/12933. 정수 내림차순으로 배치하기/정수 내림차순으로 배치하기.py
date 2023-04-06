def solution(n):
    n = list(map(int, str(n)))
    n = sorted(n, reverse=True)
    a = ''
    for i in n:
        a += str(i)
    return int(a)