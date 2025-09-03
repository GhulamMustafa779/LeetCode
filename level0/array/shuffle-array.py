def shuffle(nums: list[int], n: int) -> list[int]:
    res = []
    for i in range(n):
        res.append(nums[i])
        res.append(nums[n + i])

    return res


print(shuffle([1,2,3,4,4,3,2,1],4))