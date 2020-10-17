#This version didn't pass the time limit test
#but solution works in general
'''Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:          Output:
[[0,0,0],       [[0,0,0],
 [0,1,0],        [0,1,0],
 [0,0,0]]        [0,0,0]]

 Example 2:
Input:          Output:
[[0,0,0],       [[0,0,0],
 [0,1,0],       [0,1,0],
 [1,1,1]]       [1,2,1]]

Hint: use BFS, DFS
I prefer DP solution
'''
                    
                    
def updateMtrx(a):
    rows = len(a)
    cols = len(a[0])
    #new_array = [[0 for i in range(cols)] for j in range(rows)] 
    def get_neighbors(y, x, H, W):
        neighbors = []
        dictionary = {'left': (y, x-1),
        'right': (y, x+1),
        'top': (y+1, x),
        'bottom': (y-1, x)}
        for key, value in dictionary.items():
            zero, one = value
            if 0<=zero<H and 0<=one<W:
                neighbors.append(value)
        return neighbors

    def dfs(i,j,visited, arr):
        if (i,j) not in visited:
            visited.append((i,j))
        queue.append((i,j))
        neighbors = get_neighbors(i, j, rows, cols)
        vals =[]
        while queue:
            s = queue.pop(0)
            for z in neighbors:
                c, d = z
                vals.append(arr[c][d])
            if 0 in vals:
                    state = True
            else:
                for z in neighbors:
                    c,d = z
                    if(z not in visited):
                        dfs(c,d, visited, arr)
                vals = []
                for z in neighbors:
                    c, d = z
                    vals.append(arr[c][d])   
                arr[i][j]=min(vals)+1
    
    state = True
    visited = []
    queue = []
    while state:
        state = False
        for i in range(rows):
            for j in range(cols):
                if a[i][j] >= 1:
                    dfs(i,j,visited, a)
    return a


test1 = [[0,0,0],       
 [0,1,0],        
 [0,0,0]]        

test2 = [[0,0,0],       
 [0,1,0],       
 [1,1,1]]       

test3 = [[1,2,3],       
 [4,5,6],        
 [7,8,9]]

test4 = [[0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,1,0]]

test5=[[0],[1]]

test6 = [
[0,1,0,1,0,1,0,0,1,1],
[1,0,0,0,1,1,1,1,0,1],
[1,1,1,1,1,1,1,0,1,0],
[1,1,1,1,0,1,0,0,1,1]]

test6result = [
    [0,1,0,1,0,1,0,0,1,1],
    [1,0,0,0,1,2,1,1,0,1],
    [2,1,1,1,1,2,1,0,1,0],
    [3,2,2,1,0,1,0,0,1,1]]

print(updateMtrx(test4))