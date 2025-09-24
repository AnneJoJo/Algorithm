def solution(self,ss, ranges):
    n = len(ss) Idx =[0] * n Chars=[] starCount = 0 res = []
    for i in range(n):
        Idx[i] = len(Chars) 
        if ss[i] == '|':
            if not Chars:
                if ss[0]!='|' : 
                    starCount = 0 Chars.append(starCount)
            else:
                Chars.append(starCount + Chars[-1])
                starCount = 0 
        else:
            starCount += 1 
    for begin, end in ranges:
        if begin<0 orbegin>=norend<0 orend>=n: 
            res.append(-1)
            continue
        beginIdx = Idx[begin] 
        endIdx = Idx[end]
        if ss[end]!='|':
            endIdx -=1
        if endIdx > beginIdx :
            res.append(Chars[endIdx] - Chars[beginIdx])
        else:
            res.append(0) 
    return res