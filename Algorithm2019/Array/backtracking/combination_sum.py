def combination_sum(n):

    if n == 0:
        return 0
    res =[]
    dfs(n,'',res)
    return res

def dfs(n,sub,res):

    if n == 0:
        res.append(sub)

    for i in range(1,n+1):
        if sub and int(sub[-1])> i:
            continue
        dfs(n-i,sub + str(i),res)


print(combination_sum(5))



