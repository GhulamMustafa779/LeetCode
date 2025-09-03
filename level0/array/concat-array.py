def getConcatenation(nums: list[int]) -> list[int]:
    for i in range(len(nums)):
        nums.append(nums[i])

    return nums

print(getConcatenation([1,3,2,1]))