def solution(x):
    arr = list(str(x))
    s = 0
    for i in arr:
        s += int(i)
    if x % s == 0:
        return True
    return False