def longestRepeatSubstring(s):
    """
    0 1 2 3 4
    5 / 2 = 2 odd mid
    0 1 2 3 4 5
    6 / 2 = 3   even mid is the right in mid
     substring is decided by length such as 1, 2, 3, 4
     ex: abbbbsaaddss
     ab bb sa ad ds s
     as long as repeat item exists, count as max
     could use binary, because the longest repeat substring must be <= len(s) // 2
     s1:

    :param s:
    :return: ans
    1-0 : 2  b in a ?
    2-0 : 3  b in ab ? ans + 1 = 1
    3-1:  4  bb  in abb  ans + 1 = 2
    4-2: 5  bbb in abbb ans+1 = 3
    5-3: 6 :5 bbbs in abbbb

    """
    # s1
    n = len(s)
    ans = 0
    for i in range(1, n):
        if s[i - ans:i + 1] in s[:i]:
            ans += 1
    return ans
