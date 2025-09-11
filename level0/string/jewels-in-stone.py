def numJewelsInStones(jewels: str, stones: str) -> int:
    map = {}
    for i in range(len(jewels)):
        if jewels[i] not in map:
            map[jewels[i]] =  True
    
    count = 0
    for j in range(len(stones)):
        if stones[j] in map:
            count+=1
    
    return count


jewels = "aA"
stones = "aAAbbbb"
print(numJewelsInStones(jewels, stones))