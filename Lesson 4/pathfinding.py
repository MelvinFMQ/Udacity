# ----------
# User Instructions:
# 
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------

# Grid format:
#   0 = Navigable space
#   1 = Occupied space

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']
def exhausive(a):
    if a[1] == 1 and a[2] == 1 and a[3] == 1 and a[4] == 1:
        #print(a[1])
        #print(a[2])
        #print(a[3])
        #print(a[4])
        return True
    else:
        return False

def check_neigbour_visited(visited, coord):
    x , y = coord
    if [x + 1, y] in visited:
        return True
    elif [x - 1, y] in visited:
        return True
    elif  [x, y + 1] in visited:
        return True
    elif [x, y - 1] in visited:
        return True
    else:
        return False
def get_min(path_cost, visited):
    min_cost = 101
    for x in range(len(path_cost)):
        for y in range(len(path_cost[0])):
            if(not [x,y] in visited) and grid[x][y] != 1 and check_neigbour_visited(visited, [x,y]):
                # has not been visited and is not a wall and neibour has been visited
                #print('exhausive', exhausive(path_cost[x][y]))
                return [x, y]
    else:
        return [-1, -1]

def traverse_back(path_cost, goal, start):
    x, y = goal
    total_row = 0
    total_col = 0
    a = [] 
    while [x,y] != start:
        tmp_x = path_cost[x][y][5]
        tmp_y = path_cost[x][y][6]
        total_row += abs(tmp_x - x)
        total_col += abs(tmp_y - y)
        a.append([x,y])
        x, y= tmp_x, tmp_y
    a.append([x,y])
    return total_row, total_col, a
        
def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    x = init[0]
    y = init[1]
    max_x = len(grid) - 1 
    max_y = len(grid[0]) - 1
    path_cost = [[[100, 0, 0,0,0,0,0]  for i in range(len(grid[0]))] for i in range(len(grid))]
    path_cost[x][y] = [0, 1,1,1,1,0,0]
    for i in range(len(path_cost)): #x
        for j in range(len(path_cost[0])): #y
            if grid[i][j] == 1:
                path_cost[i][j] = [100,1, 1,1,1,0,0]
            else:
                if i == 0: #if top row 
                    path_cost[i][j][1] = 1
                elif grid[i - 1][j] == 1:
                    path_cost[i][j][1] = 1
                if j == max_y: #if right column
                    path_cost[i][j][2] = 1
                elif grid[i][j + 1] == 1: #means its not the right most, # if right is wall
                    path_cost[i][j][2] = 1
                if i == max_x: #if bottom row
                    path_cost[i][j][3] = 1
                elif grid[i + 1][j] == 1:
                    path_cost[i][j][3] = 1
                if j == 0: #if left column
                    path_cost[i][j][4] = 1
                elif grid[i][j-1] == 1:
                    path_cost[i][j][4] = 1
    #print(path_cost)
    visited = []
    sucess = True
    while not exhausive(path_cost[goal[0]][goal[1]]):
        tmp_cost = path_cost[x][y][0] + 1
        if x < max_x and grid[x + 1][y] != 1: #if it's not at the bottom most and it's not a wall, can move down
            if tmp_cost < path_cost[x + 1][y][0]:
                path_cost[x + 1][y][0] = tmp_cost
                path_cost[x + 1][y][5] = x
                path_cost[x + 1][y][6] = y
            path_cost[x + 1][y][1] = 1 #element is visted from the top
        if x > 0 and grid[x -1][y] != 1: #if it's not at the top most and it's not a wall, can move up
            if tmp_cost < path_cost[x - 1][y][0]:
                path_cost[x - 1][y][0] = tmp_cost
                path_cost[x - 1][y][5] = x
                path_cost[x - 1][y][6] = y
            path_cost[x - 1][y][3] = 1 #element is visited from the bottom
        if y < max_y and grid[x][y + 1] != 1: #if it's not at the right most and it's not a wall, can move left
            if tmp_cost < path_cost[x][y + 1][0]:
                path_cost[x][y + 1][0] = tmp_cost
                path_cost[x][y + 1][5] = x
                path_cost[x][y + 1][6] = y
            path_cost[x][y + 1][2] = 1 #element is visited from the right
        if y > 0 and grid[x][y - 1] != 1: #if it's not at left most and it's not a wall, can move right
            if tmp_cost < path_cost[x][y - 1][0]:
                path_cost[x][y - 1] = tmp_cost
                path_cost[x][y - 1][5] = x
                path_cost[x][y - 1][6] = y
            path_cost[x][y - 1][4] = 1 #element is visited from the left
        #print('now', x,y)
        visited.append([x,y])
        x, y = get_min(path_cost, visited)
        if x == -1:
            sucess = False
        #print('next', x,y)
        #print(path_cost[x][y])
        #print_path(path_cost)
        #print('visited', visited)
    if sucess == False:
        return 'fail'
    else:
        minimum_cost = path_cost[goal[0]][goal[1]][0]
        row, col , a = traverse_back(path_cost, goal, init)
        return path[minimum_cost] + goal
            
def print_path(path_cost):
    for element in path_cost:
        print()
        print(element)

        

    
search(grid, init, goal, cost)
