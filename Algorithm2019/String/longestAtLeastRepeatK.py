import collections
# sliding window:
# class Solution {
# public:
#     int longestSubstring(string s, int k) {
#         int countMap[26];
#         int maxUnique = getMaxUniqueLetters(s);
#         int result = 0;
#         for (int currUnique = 1; currUnique <= maxUnique; currUnique++) {
#             // reset countMap
#             memset(countMap, 0, sizeof(countMap));
#             int windowStart = 0, windowEnd = 0, idx = 0, unique = 0, countAtLeastK = 0;
#             while (windowEnd < s.size()) {
#                 // expand the sliding window
#                 if (unique <= currUnique) {
#                     idx = s[windowEnd] - 'a';
#                     if (countMap[idx] == 0) unique++;
#                     countMap[idx]++;
#                     if (countMap[idx] == k) countAtLeastK++;
#                     windowEnd++;
#                 }
#                 // shrink the sliding window
#                 else {
#                     idx = s[windowStart] - 'a';
#                     if (countMap[idx] == k) countAtLeastK--;
#                     countMap[idx]--;
#                     if (countMap[idx] == 0) unique--;
#                     windowStart++;
#                 }
#                 if (unique == currUnique && unique == countAtLeastK)
#                     result = max(windowEnd - windowStart, result);
#             }
#         }

#         return result;
#     }

#     // get the maximum number of unique letters in the string s
#     int getMaxUniqueLetters(string s) {
#         bool map[26] = {0};
#         int maxUnique = 0;
#         for (int i = 0; i < s.length(); i++) {
#             if (!map[s[i] - 'a']) {
#                 maxUnique++;
#                 map[s[i] - 'a'] = true;
#             }
#         }
#         return maxUnique;
#     }
# };
 #brute force
 
class Solution(object):
    def longestSubstring(self, s, k):
       
        self.length = 0
        def isValid(s,k):
           
            dic = collections.Counter(s)
            for key, val in dic.items():
                if val < k:
                    return False
            return True
        for step in range(len(s)):
            for start in range(len(s)-step):
                if isValid(s[start:start+step+1],k):
                    self.length = max(self.length, len(s[start:start+step+1]))
            

        return self.length
    
# divide and conqure

# class Solution {
#     public:
#     int longestSubstring(string s, int k) {
#         int n = s.size();
#         return longestSubstringUtil(s, 0, n, k);
#     }
#     int longestSubstringUtil(string &s, int start, int end, int k) {
#         if (end < k) return 0;
#         int countMap[26] = {0};
#         // update the countMap with the count of each character
#         for (int i = start; i < end; i++)
#             countMap[s[i] - 'a']++;
#         for (int mid = start; mid < end; mid++) {
#             if (countMap[s[mid] - 'a'] >= k) continue;
#             int midNext = mid + 1;
#             while (midNext < end && countMap[s[midNext] - 'a'] < k) midNext++;
#             return max(longestSubstringUtil(s, start, mid, k),
#                     longestSubstringUtil(s, midNext, end, k));
#         }
#         return (end - start);
#     }
# };
