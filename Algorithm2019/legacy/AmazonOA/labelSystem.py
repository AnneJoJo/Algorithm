import collections
class LabelingSystem(object): 
    def solution(self, s, k):
        chrCounts = collections.Counter(s)
        chrs = [[c,chrCounts[c]] for c in chrCounts] 
        chrs.sort(reverse= True)
        i,n =0,len(chrs)
        res=[]
        while i < n:
            if chrs[i][1] > k: 
                res.append(chrs[i][0]*k) 
                chrs[i][1] -= k
                j = i+1
                while j<n and chrs[j][1] <= 0: 
                    j+=1
                if j < n and chrs[j][1] > 0: 
                     res.append(chrs[j][0]) 
                     chrs[j][1] -= 1
                else: 
                    break
            elif chrs[i][1] > 0: 
                res.append(chrs[i][0]*chrs[i][1]) 
                chrs[i][1] = 0
            else :
                i+=1 
        return "".join(res)
l = LabelingSystem()
print(l.solution("zzzzzzxxxzzaabbazza", 3))