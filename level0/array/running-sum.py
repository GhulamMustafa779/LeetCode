def runningSum(nums: list[int]) -> list[int]:
    sum = 0
    for i,n in enumerate(nums, start=0):
        sum = sum + n
        print(sum)
        nums[i] = sum
        
    return nums



print(runningSum([1,2,3,4]))