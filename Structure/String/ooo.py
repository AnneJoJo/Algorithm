class solution:
    def count_secret_pairs(self,upperBound,lowerBound,consecutiveDifference):
        # Initial Variable Setting
        highest_sum = lowest_sum = sum = 0
        for value in consecutiveDifference:
            sum += value
            highest_sum = max(sum, highest_sum)
            lowest_sum = min(sum, lowest_sum)

        # Need to +1 because of combination  = difference +1 ( count of ([2,3,4,5]) = (5-2) +1)
        result = (upperBound - lowerBound + (lowest_sum - highest_sum + 1))
        if result < 0:
            # Correction suggestion from @rvlyanon, thanks!
            return 0
        else:
            return result

# Test code
consecutiveDifference = [1, 2]
lowerBound = 3
upperBound = 4
sol = solution()
print(sol.count_secret_pairs(upperBound, lowerBound, consecutiveDifference))
# return 3

# consecutiveDifference = [1, 1, 1, 1]
# sol.count_secret_pairs(upperBound, lowerBound, consecutiveDifference)
# # return 4