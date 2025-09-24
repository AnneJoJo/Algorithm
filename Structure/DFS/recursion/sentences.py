class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        brute force 
        recursive 
        atom question what if one row and col can definitely cover the word
        what if not?
        """
        def canWordFitIn(word, cols):
            
            if len(word) <= cols:
                return True
            else:
                return False
            
        self.k = 0
        def recursiveBuild(sentence,k,rows, cols,curLevel):
           
        
            if rows == 0:
                self.k = max(self.k, k-1)
                return 
            
            word = sentence[k%len(sentence)]

            newCurLevel = curLevel + word+'-'
         
            if (len(newCurLevel) - 1) == cols:
                newCurLevel = newCurLevel[:-1]
            
            doesFit = canWordFitIn(newCurLevel, cols)
            
            if doesFit:
               
                recursiveBuild(sentence,k+1,rows, cols, newCurLevel)
            else:
                   
                recursiveBuild(sentence,k+1,rows-1, cols, word+'-')
                    
            
            return 
        recursiveBuild(sentence, 0, rows, cols,'')
       
        return (self.k) // len(sentence)