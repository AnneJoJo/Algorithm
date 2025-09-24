class MaxShipping(object):
     def maxShippingDist(self,A, B, maxDist):
        if not A or not A[0] :
            return [] 
        if not B or not B[0]:
            return []
        res = []
        target = 0
        A.sort(key=lambda x:x[1])
        B.sort(key=lambda x:x[1],reverse=True)
        m,n=len(A),len(B)
        i = 0
        j = 0
        retValue = 0
        while i < m and j < n:
            tmpSum = A[i][1] + B[j][1]
            if tmpSum > maxDist:
                j+=1
            elif tmpSum < maxDist:
                if tmpSum > retValue:
                    retValue = tmpSum
                    res = [A[i][0],B[j][0]]
                i+=1
            else:
                retValue = maxDist
                res.append([A[i][0],B[j][0]])
                i,j=i+1,j+1
        return res
list1 = [[1, 8], [2, 15], [3, 9]]
list2 = [[1, 8], [2, 11], [3, 12]]
m = MaxShipping()
print(m.maxShippingDist(list1,list2,20))   
        
        