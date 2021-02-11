class Solution:
    def duplicateZeros(self, arr):
        """
        Do not return anything, modify arr in-place instead.
        """

        # possible_dups = 0
        # length_ = len(arr) - 1

        # # Find the number of zeros to be duplicated
        # for left in range(length_ + 1):

        #     # Stop when left points beyond the last element in the original list
        #     # which would be part of the modified list
        #     if left > length_ - possible_dups:
        #         break

        #     # Count the zeros
        #     if arr[left] == 0:
        #         # Edge case: This zero can't be duplicated. We have no more space,
        #         # as left is pointing to the last element which could be included  
        #         if left == length_ - possible_dups:
        #             arr[length_] = 0 # For this zero we just copy it without duplication.
        #             length_ -= 1
        #             break
        #         print(possible_dups)
        #         possible_dups += 1 # trick 

        # # Start backwards from the last element which would be part of new list.
        # last = length_ - possible_dups
        # print(arr)

        # # Copy zero twice, and non zero once.
        # print(last, possible_dups)
        # for i in range(last, -1, -1):
        #     if arr[i] == 0:
        #         arr[i + possible_dups] = 0
        #         possible_dups -= 1
        #         arr[i + possible_dups] = 0
        #     else:
        #         arr[i + possible_dups] = arr[i]

        ####---------own method---------##################
        #### edge case-----------------------#############
        countZero = 0
        length = len(arr)
        for left in range(len(arr)):


            if arr[left] == 0:
                if(left == len(arr)-1):
                    length -= 1

                    countZero += 1
                else:
                    length -= 2
                    countZero += 1

            if arr[left] != 0:
                length -= 1
            
            if length <=0:
                break


        emptySpace = len(arr) -1 - left
        left += length
        
        print(arr, left, emptySpace, length,'hi')
        
        if countZero == 0 or left == len(arr) -1:
            return arr


        for i in range(left+1, len(arr)): # decrease mush use -1
            arr[i] = 0


        p2 = left 
    
        for j in range(left, -1, -1):

            if arr[j] == 0:
                arr[j + emptySpace] = 0
                emptySpace -= 1
                arr[j + emptySpace] = 0
            else:
                arr[j + emptySpace] = arr[j]

        print(arr,'final')

s = Solution()
s.duplicateZeros([1,1,2,0])