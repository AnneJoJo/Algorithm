class NearestCities(object):
    def solution(self, points, xCoord, yCoord, queriedPoints):
        n = len(points)
        mpx= collections.defaultdict(set) 
        mpy= collections.defaultdict(set) 
        coord = collections.defaultdict(list) for i in range(n):
        p, x, y = points[i], xCoord[i],yCoord[i] coord[p]=[x, y]
        mpx[x].add(p)
        mpy[y].add(p)
        res=[]
        for p in queriedPoints:
            dest='NONE'
            x , y = coord[p] dist = float('inf')
        for p_x in mpx[x]: 
            if p_x != p:
                if dist > abs(coord[p_x][1] - y): 
                    dist = abs(coord[p_x][1] - y) 
                    dest = p_x
        for p_y in mpy[y]: 
            if p_y != p:
                if dist > abs(coord[p_y][0]-x): 
                    dist = abs(coord[p_y][0]-x) 
                    dest = p_y
        res.append(dest) 
        
    return res