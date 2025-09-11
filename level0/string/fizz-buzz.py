def fizzBuzz(n: int) -> list[str]:
    res = []
    for i in range(n):
        res.append("")
        flag = False
        if (i+1) % 3 == 0:
            res[i] += "Fizz"
            flag = True
        if (i+1) % 5 == 0:
            res[i] += "Buzz"
            flag = True
        if flag == False:
            res[i] = str(i+1)
    
    return res

print(fizzBuzz(15))