class RoverControl(object):
    def solution(self, A, cmds):
        dir = {'RIGHT':(0,1), 'DOWN':(1,0), 'LEFT':(0,-1), 'UP':(-1,0)}
        m, n = len(A),len(A[0])
        row,col = 0, 0
        for cmd in cmds:
            dr,dc = dir[cmd]
            newRow =row+dr
            newCol =col+dc
            if newRow<0 or newRow >= m or newCol<0 or newCol>=n:
                continue
            row = newRow
            col = newCol 
        return A[row][col]
    
r = RoverControl()
print(r.solution([[0,1,2,3],[4,5,6,7],[8,9,10,11],[12,13,14,15]], ['RIGHT', 'UP', 'DOWN', 'LEFT', 'DOWN', 'DOWN']))