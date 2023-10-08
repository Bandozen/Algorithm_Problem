def cntDivisor(n):
    cnt = 0
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            cnt += 1
            if((i**2) != n):
                cnt += 1
                
    return cnt

def solution(number, limit, power):
    answer = 0
    cntDivisorList = []
    for i in range(1, number+1):
        cntDivisorList.append(cntDivisor(i))
    for i in range(0, len(cntDivisorList)):
        if cntDivisorList[i] > limit:
            answer += power
        else:
            answer += cntDivisorList[i]
    return answer