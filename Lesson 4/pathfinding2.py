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
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 1, 1, 0],
        [0, 0, 1, 0, 1, 0]]
init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open_a = [init]
    flags = [False] #close flags for open elements
    g_values = [[-1 for i in range(len(grid[0]))] for i in range(len(grid))]
    g_values[init[0]][init[1]] = 0
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    while False in flags: #while there are open elements that have not been closed.
        min_g_index = 0
        while flags[min_g_index] == True:
            min_g_index += 1
        #expansion
        x, y = open_a[min_g_index]
        new_g_value = g_values[x][y]
        for deltax, deltay in delta:
            tmp_x = deltax + x
            tmp_y = deltay + y
            if tmp_x > max_x or tmp_x < 0 or tmp_y > max_y or tmp_y < 0 or grid[tmp_x][tmp_y] == 1:
                #if x or y is to small or big or is a wall
                pass
                #print('x', deltax , 'y', deltay)
            else:
                old_g_value = g_values[tmp_x][tmp_y]
                if old_g_value == -1: #first g_value
                    g_values[tmp_x][tmp_y] = new_g_value + cost
                    open_a.append([tmp_x,tmp_y])
                    flags.append(False)
                elif old_g_value > new_g_value + cost: #if new g_value is lower, replace 
                    g_values[tmp_x][tmp_y] = new_g_value + cost
                #if its the goal, end.
                if [tmp_x,tmp_y] == goal:
                    print(g_values)
                    return [g_values[tmp_x][tmp_y], tmp_x, tmp_y]
        #flaging node is no open.
        flags[min_g_index] = True
    return 'fail'

print(search(grid,init,goal,cost))
