def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    l1 = len(word1)
    l2 = len(word2)
    max_len = max(l1 ,l2)
    for i in range(max_len):
        if i < l1:
            res += word1[i]
        if i < l2:
            res += word2[i]
    
    return res


word1 = "abcd"
word2 = "pq"
print(mergeAlternately(word1, word2))