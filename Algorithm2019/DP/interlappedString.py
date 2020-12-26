class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        cache = set()
        if l1 + l2 != l3:
            return False

        def dfsCheck(i, j):

            if (i + j) >= l3:
                return True
            if (i, j) in cache:
                return False
            cache.add((i, j))
            if i < l1 and s1[i] == s3[i + j]:
                res1 = dfsCheck(i + 1, j)
                if res1: return True
            if j < l2 and s2[j] == s3[i + j]:
                res2 = dfsCheck(i, j + 1)
                if res2: return True

        return dfsCheck(0, 0)

