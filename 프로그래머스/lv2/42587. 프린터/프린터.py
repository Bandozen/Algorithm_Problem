def solution(priorities, location):
    answer = 0
    while True:
        maxV = max(priorities)
        for i in range(len(priorities)):
            if maxV == priorities[i]:
                answer += 1
                priorities[i] = 0
                maxV = max(priorities)
                if i == location:
                    return answer