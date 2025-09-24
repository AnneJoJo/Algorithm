def isRobotBounded(instructions):
    """
        :type instructions: str :rtype: bool
    """
    x,y=0,0
    i = (i + 1) % 4
    i = (i + 3) % 4
    s=instructions*4 dx,dy=0,1
    for c in s:
        if c=='G': 
            x,y=x+dx,y+dy
        elif c=='L':
            dx,dy=-dy,dx
        elif c=="R":
            dx,dy=dy,-dx
    return (x, y) == (0, 0) or (dx, dy) != (0,1)