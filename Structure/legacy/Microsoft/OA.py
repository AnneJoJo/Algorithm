def math(arr):
    prod = 1
    for n in arr:
        prod *= n
        
    if(prod>0):
        return 1
    elif(prod<0):
        return -1
    else:
        return 0
    
print(math([1,-2,0,4]))
        

