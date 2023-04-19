def solution(price, money, count):
    answer = 0
    sumV = 0
    for i in range(1, count+1):
        sumV += price * i
    if sumV < money:
        answer = 0
    else:
        answer = sumV - money
    return answer