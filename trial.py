def getResult(total, totalN, memo):
    if total == 0:
       result[0] += 1
    if total in memo:
        return


    if total < 0:
        return

    memo[total] = 0
    for n in totalN:
        getResult(total - n, totalN, memo)

result = [0]
total = 5
totalN = []
memo = {}
getResult(total, totalN, memo)


return result[0]
