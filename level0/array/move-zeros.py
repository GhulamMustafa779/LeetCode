def moveZeroesOne(nums: list[int]) -> None:
    size = len(nums)
    if size <= 1:
        return

    for i in range(size-1, -1, -1):
        if nums[i] == 0:
            for j in range(i+1, size):
                if nums[j] != 0:
                    nums[j-1] = nums[j]
                    nums[j] = 0
    
# efficient solution
def moveZeroesTwo(nums: list[int]) -> None:
    prev_non_zero = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            temp = nums[prev_non_zero]
            nums[prev_non_zero] = nums[i]
            nums[i] = temp
            prev_non_zero += 1



array = [0,1,0,3,12]
print('before',array)
moveZeroesTwo(array)
print('after',array)