# class Options:
#     def shoppingOptions(self, priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops,dollars):
#         self.count = 0
#         def backTracking(arr,start,total):
        
#             if start == 4 and total >=0:
#                 self.count+=1
#                 return 
#             elif total < 0:
#                 return 
#             prices = arr[start]
        
#             for each in prices:
                
#                 backTracking(arr,start+1,total-each) 
                
#             return self.count
#         arr = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]
#         backTracking(arr,0, dollars)
#         return self.count
# O = Options()
# print(O.shoppingOptions([2, 3], [4], [2, 3], [1, 2], 10))
# print(O.shoppingOptions([2, 3], [4], [2, 3], [1, 2], 9))
# print(O.shoppingOptions([6], [1, 1, 1, 1], [4, 5, 6], [1], 13)) 
# print(O.shoppingOptions([6], [1, 1, 1, 1], [4, 5, 6], [1], 14)) 
# print(O.shoppingOptions([100], [1, 1, 1, 1], [4, 5, 6], [1], 99)) 
# print(O.shoppingOptions([1], [1], [1], [1], 4)) 
# assert self.solution([6], [1, 1, 1, 1], [4, 5, 6], [1], 13) == 8
# assert self.solution([6], [1, 1, 1, 1], [4, 5, 6], [1], 14) == 12
# assert self.solution([100], [1, 1, 1, 1], [4, 5, 6], [1], 99) == 0
# assert self.solution([1], [1], [1], [1], 4) == 1
# assert self.solution([1], [1], [1], [1], 3) == 0


def shoppingOptions(priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops,dollars):
        def backTracking(arr,start,total):
        
            if start == 4 and total >=0:
                return 1
            elif total < 0:
                return 0
            prices = arr[start]
            res = 0
            for each in prices:
                
               res += backTracking(arr,start+1,total-each)
                
            return res
        arr = [priceOfJeans, priceOfShoes, priceOfSkirts, priceOfTops]
        
        return backTracking(arr,0, dollars)
    
print(shoppingOptions([2, 3], [4], [2, 3], [1, 2], 10))
