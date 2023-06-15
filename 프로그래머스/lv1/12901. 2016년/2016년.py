def solution(a, b):
    days = ['SUN','MON','TUE','WED','THU','FRI','SAT']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    answer = days[(sum(months[:a-1]) + b) % 7 - 3]
    return answer