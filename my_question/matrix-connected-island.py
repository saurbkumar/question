# find the number of connected island

grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,1,1,0,0],
        [0,0,0,1,1]]
storeCount = 0
x_length = len(grid)
y_length = len(grid[0])
def getNextLocation(i,j,x_length,y_length):
    nextLocation = []
    for temp in [(1,0),(-1,0), (0,1), (0,-1)]:
        if (i + temp[0]<x_length and i + temp[0]>-1) and (j + temp[1]<y_length and j + temp[0]>-1):
            next_i, next_j = i + temp[0], j + temp[1]
            nextLocation.append([next_i, next_j])
    return nextLocation
#def search(grid, i j):
visited = set()
from collections import deque
for i in range(x_length):
    for j in range(y_length):
        if grid[i][j]==0 or (i,j) in visited:
            continue
        visited.add((i,j))
        storeCount += 1
        for nextLocation in getNextLocation(i,j,x_length,y_length):
            stack =deque()# search for next
            if grid[nextLocation[0]][nextLocation[1]]!=0 and (nextLocation[0], nextLocation[1]) not in visited:
                stack.append(nextLocation)
            while len(stack):
                currentNode = stack.pop();
                visited.add((currentNode[0],currentNode[1]))
                for next_ in getNextLocation(currentNode[0], currentNode[1], x_length,y_length):
                    if grid[next_[0]][next_[1]]!=0 and (next_[0],next_[1]) not in visited:
                        stack.append(next_)
                        
                                    
print(storeCount)
