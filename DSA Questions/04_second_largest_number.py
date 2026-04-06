def find_second_largest(nums:list) -> int:
    first = float('-inf')
    second = float('-inf')

    for num in nums:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float('-inf'):
        return None
    
    return second            




nums = [10, 4, 7, 9, 12, 12]
print(find_second_largest(nums))




'''
def find_second_largest(nums:list) -> int:
    if len(nums) < 2:
        return None
    nums = list(set(nums))
    nums.sort()

    return nums[-2]
'''