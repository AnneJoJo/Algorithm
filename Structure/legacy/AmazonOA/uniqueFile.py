import collections
class UniqueFileNames(object): 
    def solution(self, names):
        nameCnt = collections.defaultdict(int) 
        res=[]
        for name in names:
            if name not in nameCnt: 
                res.append(name)
                nameCnt[name] = 1 
            else:
                res.append(name+str(nameCnt[name])) 
                nameCnt[name] +=1 
        return res
u = UniqueFileNames()    
print(u.solution(["system","access","access","system","access","access"]))
