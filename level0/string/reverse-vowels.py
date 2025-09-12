def reverseVowels(s: str) -> str:
    l = 0
    r = len(s) - 1

    res = list(s)
    vowels = ["a","e","i","o","u"]

    # while l < r:
    #     if s[l].lower() not in vowels:
    #         l += 1
    #     elif s[r].lower() not in vowels:
    #         r -= 1
    #     else:
    #         res[l], res[r] = res[r], res[l]
    #         l += 1
    #         r -= 1

    while l < r:
        while l < r and s[l].lower() not in vowels:
            l += 1
        while l < r and s[r].lower() not in vowels:
            r -= 1
        res[l], res[r] = res[r], res[l]
        l += 1
        r -= 1

    
    return "".join(res)

s = "leetcode"
print(reverseVowels(s))
