import collections
class WinningSequence(object):
    def solution(self, n, low, hi):
        dq=collections.deque([hi]) 
        n-=1
        num = hi
        while n>0:
            num -= 1
            if num < low:
                return [] 
            dq.append(num)
            n-=1 
            if n>0:
                dq.appendleft(num) 
            n-=1
        return list(dq)
w = WinningSequence() 
print(w.solution(4,10,12))