def removeDupFromSorted(arr):
	'''
		inplace 0,0,1,1,1,2,2,3,3,4

		0 1 2 3 1 2 2 3 3 4 
	'''
	slow  = 0

	for i in range(1,len(arr)):

		if arr[i-1] != arr[i]:
			arr[slow] = arr[i-1]
			slow += 1
		if i == len(arr) - 1:
			arr[slow] = arr[i]

	print(arr[:slow+1])


removeDupFromSorted([0,0,1])


# public int removeDuplicates(int[] nums) {
#     if (nums.length == 0) return 0;
#     int i = 0;
#     for (int j = 1; j < nums.length; j++) {
#         if (nums[j] != nums[i]) {
#             i++;
#             nums[i] = nums[j];
#         }
#     }
#     return i + 1;
# }



