class OptimizatingBoxWeight(object): 
    def solution(self, arr):
        arr.sort(reverse=True) 
        total =sum(arr)
        res =[]
        sumA = 0
        for i in range(0,len(arr)): 
            res.append(arr[i])
            sumA +=arr[i]
            sumB = total - sumA
            if sumA > sumB:
                break
        return res[::-1] 

def test(self):
    res = self.solution([5, 3, 2, 4, 1, 2]) 
    print(res)