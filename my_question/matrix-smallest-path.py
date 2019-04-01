from collections import deque
maze =[[0, 0, 1],
       [0, 0, 1],
       [0, 0, 0]]



def memoize(f):
    """ Memoization decorator for functions taking one or more arguments. """
    class memodict(dict):
        def __init__(self, f):
            self.f = f
        def __call__(self, *args):
            return self[args]
        def __missing__(self, key):
            ret = self[key] = self.f(*key)
            return ret
    return memodict(f)
@memoize
def expandable_nodes(maze_dim, current_pos):
    neighbors = [
                [current_pos[0]-1, current_pos[1]],
                [current_pos[0], current_pos[1]-1],
                [current_pos[0], current_pos[1]+1],
                [current_pos[0]+1, current_pos[1]]]
    expandable_node = deque()
    for neighbor in neighbors:
        if neighbor[0] <= maze_dim[0] and neighbor[0]>=0 and neighbor[1] <= maze_dim[1] and neighbor[1]>=0:
            expandable_node.append(neighbor)
    return expandable_node


total_path = deque()

temp_maze = maze
maze_dim = (len(temp_maze)-1, len(temp_maze[0])-1)
start_point = (0,0)
end_pos = (len(maze)-1,len(maze[0])-1)
visited = [[False] * (maze_dim[1] + 1) for _ in range(maze_dim[0] + 1)]
path_len_matrix = [[0] * (maze_dim[1] + 1) for _ in range(maze_dim[0] + 1)]

# from start position                   
stack_ = deque()
stack_.append(start_point)
while stack_:
    current_position = stack_.popleft()
    neighbors = expandable_nodes(maze_dim,(current_position[0],current_position[1]))
    for neighbour in neighbors:
        #if neighbour
        if (not visited[neighbour[0]][neighbour[1]] and temp_maze[neighbour[0]][neighbour[1]]!= 1):#node is not visited yet
            if not neighbour==end_pos:# will not append the end point in the stack
                stack_.append(neighbour)
                path_len_matrix[neighbour[0]][neighbour[1]]=path_len_matrix[current_position[0]][current_position[1]]+1 # update all neighbour value by one i.e updating the path value 
    visited[current_position[0]][current_position[1]] = True #mark current position as yes
if visited[end_pos[0]][end_pos[1]]:# i.e last point visited
    total_path.append(path_len_matrix[end_pos[0]][end_pos[1]])
#print(min(total_path)) + 1
