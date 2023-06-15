def solution(nums):
    phoneketmon_type = len(set(nums))
    if phoneketmon_type < len(nums) // 2:
        return phoneketmon_type
    else:
        return len(nums) // 2