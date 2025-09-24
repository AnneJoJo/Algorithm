# Approach One DFS+ fisher random
def generateMazeDFSApproach(start, end):
    '''
    1. use dfs to generate a path from start to end
    2. random pick the cells as blocker
    
    '''
    
    
# Approach Two: Union find

def mazeUnionFind(start, end, height, width):
    '''
    1. generate a matrix with h*w and enumerate each cell
    2. save all connections in the set, which cell is adjacent with the current one (2,3)
    3. Initilaze all cells number with root array [0,1,2,3..]
    4. random pop up the edge/adjacent from the set
    5. if they are not a union, make them as a union, also check if the cycle is generated, add them to connected set
    6. unitl the connected set has all nodes. (there will be a path for start to end)
    7, now you have all the conditons, you can print the maze with this conditions.Draw it
    
    '''
    