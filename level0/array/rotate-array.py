def rotate( nums: list[int], k: int) -> None:
    r = k % len(nums)
    for i in range(r):
        last_item = nums.pop()
        nums.insert(0, last_item)

nums=[1,2,3,4,5,6,7]
k = 3
#rotate(nums, k)
l = len(nums)
r = k % l
nums[:] = nums[l-r:] + nums[:l-r]
print(nums)


