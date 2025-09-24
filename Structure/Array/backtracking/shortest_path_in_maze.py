# backtracking for this problem is a burte force method. Clearly it's not the most optimum solution
# but we write this navie solution down for a practice.


def shortest_path_in_maze(matrix,start,end):
    """
    
    :param matrix: 2D matrix
    :param start: postion[x,y]
    :param end: position[x,y
    :return: return length of path(shortest)
    """
    res = float('inf')
    dir = [[-1,0],[0,1],[1,0],[0,-1]]
    return backtrack(start,end,[],dir,res,matrix)


def backtrack(start,end,path,dir,res,matrix):

    if start[0] < 0 or start[0] > len(matrix)-1 or start[1] < 0 or start[1] > len(matrix[0])-1 or matrix[start[0]][start[1]]=="#" or matrix[start[0]][start[1]]== 0:

        return res
    if start == end:
        res = min(res,len(path+[[start[0],start[1]]]))

        return res
    tmp=matrix[start[0]][start[1]]
    matrix[start[0]][start[1]] = "#"
    for k in dir:

        nx = start[0] + k[0]
        ny = start[1] + k[1]

        res=backtrack([nx,ny],end,path+[[nx,ny]],dir,res,matrix)
    matrix[start[0]][start[1]] = tmp
    return res



matrix = [[0,1,0,0,1],[1,1,1,0,0],[1,1,0,0,0],[1,1,0,0,1]]

print(shortest_path_in_maze(matrix,[0,1],[3,0]))