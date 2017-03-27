# -----------
# User Instructions:
#
# Modify the the search function so that it returns
# a shortest path as follows:
# 
# [['>', 'v', ' ', ' ', ' ', ' '],
#  [' ', '>', '>', '>', '>', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', 'v'],
#  [' ', ' ', ' ', ' ', ' ', '*']]
#
# Where '>', '<', '^', and 'v' refer to right, left, 
# up, and down motions. Note that the 'v' should be 
# lowercase. '*' should mark the goal cell.
#
# You may assume that all test cases for this function
# will have a path from init to goal.
# ----------

grid = [[0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 1, 0]]
        

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid,init,goal,cost):
    # ----------------------------------------
    # modify code below
    # ----------------------------------------
    closed = [[0 for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    previous = [[" " for row in range(len(grid[0]))] for col in range(len(grid))]
    x = init[0]
    y = init[1]
    g = 0
    g_values = [[[0,0,0] for row in range(len(grid[0]))] for col in range(len(grid))]

    open = [[g, x, y]]

    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand

    while not found and not resign:
        if len(open) == 0:
            resign = True
            return 'fail'
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            
            if x == goal[0] and y == goal[1]:
                found = True
                previous[x][y] = "*"
                for row in g_values:
                    print(row)
                print(previous)
                while [x, y] != init:
                    prev_x = g_values[x][y][1]
                    prev_y = g_values[x][y][2]
                    delta_x = x - prev_x
                    delta_y = y - prev_y
                    
                    if delta_x > 0: #move v
                        previous[prev_x][prev_y] = delta_name[2]
                        print(x,y)
                    elif delta_x < 0: #move ^
                        previous[prev_x][prev_y] = delta_name[0]
                        print(x,y)
                    elif delta_y > 0: #move >
                        previous[prev_x][prev_y] = delta_name[3]
                        print(x,y)
                    else:
                        previous[prev_x][prev_y] = delta_name[1]
                        print(x,y)
                    print(x,y , '--->', prev_x,prev_y)
                    x , y = prev_x, prev_y
                        
            else:
                for i in range(len(delta)):
                    #print('hi')
                    x2 = x + delta[i][0]
                    y2 = y + delta[i][1]
                    if x2 >= 0 and x2 < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if closed[x2][y2] == 0 and grid[x2][y2] == 0:
                            g2 = g + cost
                            open.append([g2, x2, y2])
                            closed[x2][y2] = 1
                            old_g_value = g_values[x2][y2][0]
                            #if old_g_value > g2: #if old g value at this location is more than new g_value, replace it
                            g_values[x2][y2][0]= g2
                            g_values[x2][y2][1] = x
                            g_values[x2][y2][2] = y
                                #print(g_values)
    

    return previous # make sure you return the shortest path
a = search(grid,init,goal,cost)
for row in a:
    print(row)
