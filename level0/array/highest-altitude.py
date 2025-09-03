def largestAltitude(gain: list[int]) -> int:
    max_gain = 0
    curr_height = 0
    for g in gain:
        curr_height += g
        max_gain = max(max_gain, curr_height)

    return max_gain


print(largestAltitude([-4,-3,-2,-1,4,3,2]))
