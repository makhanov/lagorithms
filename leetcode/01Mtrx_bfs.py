from collections import deque
def zero_one_matrix(matrix):
    if (matrix==None or len(matrix)==0):
        return matrix
    m = len(matrix)
    n = len(matrix[0])
    res = matrix[:]

    q=deque()

    for i in range(m):
        for j in range(n):
            if(matrix[i][j]==0):
                q.append([[i,j],0])

    dx = [1,-1,0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0 for _ in range(n+1)] for _ in range(m+1)]

    while q:
        tmp, distance = q.popleft()
        x0, y0 = tmp[0], tmp[1]

        if matrix[x0][y0] == 1:
            res
        
    