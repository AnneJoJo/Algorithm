'''
[aa, aa]
aabaaaabbaab
[]

brue force:
for original string 
if start with the other char, 
count == number of repaced string 
replace and save the rest use new string to self-call
aaaaaaabbaab
self(newS, count-1)

if count === 0;
save the rest length of the other char,maintain a min value
use memo to save the visited pattern 


dp

countB = [0,0,1,1,1,1,2,3,3,3,4]
  aabaaaabbaab  
1 001111111111
2 001111122333



'''
#      * @param str target string contains only 'a' and 'b'
#      * @param n number of mask string contains only 'a'
#      * @param m length of mask string

#  public int findNumberOfbAfterReplace(String str, int n, int m) {
#         int l = str.length();
#         int[][] dp = new int[l][n];
#         int[] countB = new int[l];
#         for (int i = 0; i < l; i++) {
#             countB[i] = (i == 0 ? 0 : countB[i - 1]) 
#                     + (str.charAt(i) == 'b' ? 1 : 0);
#         }
#  
#         for (int i = 0; i < l; i++) {
#             for (int j = 0; j < n; j++) {
#                 if (i < m) {
#                     dp[i][j] = countB[i];
#                 } else {
#                     dp[i][j] = Math.max(dp[i - 1][j],
#                             (j == 0 ? 0 : dp[i - m][j - 1]) + countB[i] - countB[i - m]);
#                 }
#             }
#         }
#  
#         return countB[l - 1] - dp[l - 1][n - 1];
#     }
