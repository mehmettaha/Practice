def fibon(x):
    res = [1,1]
    for i in range(0,x):
        res.append(res[i+1] + res[i])
    return res

print(fibon(14))