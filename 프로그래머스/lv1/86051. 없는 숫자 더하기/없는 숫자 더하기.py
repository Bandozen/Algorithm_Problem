def solution(numbers):
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    answer = []
    for i in nums:
        if i not in numbers:
            answer.append(i)
    return sum(answer)