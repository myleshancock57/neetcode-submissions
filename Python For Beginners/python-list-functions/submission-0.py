from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    length = len(nums)
    sum_nums = 0
    for i in range(length):
       sum_nums += nums[i]
    return sum_nums

def get_min(nums: List[int]) -> int:
    length = len(nums)
    min_nums = nums[0]
    for i in range(length):
        if nums[i] < min_nums:
            min_nums = nums[i]
        else:
            continue
    return min_nums        

def get_max(nums: List[int]) -> int:
    length = len(nums)
    max_nums = nums[0]
    for i in range(length):
        if nums[i] > max_nums:
            max_nums = nums[i]
        else:
            continue
    return max_nums

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
