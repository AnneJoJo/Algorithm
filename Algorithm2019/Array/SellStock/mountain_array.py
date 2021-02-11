
def validMontainArray(arr):
	# wrong method can't handle the plateaus
	# count = 0
	# for i in range(1,len(arr)-1):

	# 	if arr[i-1] <= arr[i] and arr[i] >= arr[i+1]:
	# 		count += 1
	
	# return True if count == 1 else False

	i = 0
        
    while i < len(arr) -1 and arr[i] < arr[i+1]:
        i += 1
            
    if i == 0 or i == len(arr) - 1:
        return False
    while i < len(arr)-1 and arr[i] > arr[i+1]:
        i += 1
            
            
            
    return i == len(arr) - 1





print(validMontainArray([0,2,3,4,5,2,1,0]))

# wrong method : didn't notice the order, it will pass for valley too.
# increase = 0
#         decrease = 0
#         for i in range(1,len(arr)):
#             if arr[i-1] < arr[i]:
#                 increase += 1
#             elif arr[i-1] > arr[i]:
#                 print(arr[i-1],arr[i])
#                 decrease += 1
                
#         total = increase + decrease
#         #print(increase, decrease)
#         return True if total + 1 == len(arr) and increase > 0 and decrease > 0 else False


# JS:
# var validMountainArray = function(arr) {
#     let increasing = arr[1] > arr[0]
#     if (!increasing) {
#         return false
#     }
#     for(let i=1; i < arr.length; i++) {
#         if (arr[i-1] === arr[i]){
#             return false
#         }
#         if(increasing) {
#             if (arr[i] < arr[i-1]) {
#                 increasing = false
#             }
#         }
#         else {
#             if(arr[i] > arr[i-1]){
#                 return false
#             }
#         }
#     }
#     return !increasing
    
# };