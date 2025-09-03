def sortedSquares(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums[i] = nums[i]**2

    nums.sort()
    return nums

    
print(sortedSquares([-4,-1,0,3,10]))