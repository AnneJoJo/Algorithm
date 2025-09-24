def breakPalindrome(self, s): 
    """
        Check half of the string,
        replace a non 'a' character to 'a'.
        If only one character, return empty string. Otherwise repalce the last character to 'b'
        Complexity
        Time O(N)
        Space O(N)  
    """
    for i in range(len(s) // 2): 
        if s[i] != 'a':
            return s[:i] + 'a' + s[i + 1:] 
        
    return s[:-1] + 'b' if s[:-1] else ''