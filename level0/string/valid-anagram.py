def isAnagram(s: str, t: str) -> bool:
    l1 = len(s)
    l2 = len(t)
    if l1 != l2:
        return False

    map = {}
    for i in range(l1):
        if s[i] in map:
            map[s[i]] += 1
        else:
            map[s[i]] = 1
    
    for j in range(l1):
        if t[j] in map:
            map[t[j]] -= 1
        else:
            return False
    
    for key in map:
        if map[key] != 0:
            return False
    
    return True

# more efficient solution
def isAnagramEff(s: str, t: str) -> bool:
    l1 = len(s)
    l2 = len(t)
    if l1 != l2:
        return False
        
    arr = [0] * 26
    for i in range(l1):
        arr[ord(s[i]) - ord('a')] += 1
        arr[ord(t[i]) - ord('a')] -= 1

    for n in arr:
        if n > 0:
            return False
    
    return True

s = "anagram"
t = "nagaram"

print(isAnagramEff(s,t))