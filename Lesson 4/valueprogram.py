# ----------
# User Instructions:
# 
# Create a function compute_value which returns
# a grid of values. The value of a cell is the minimum
# number of moves required to get from the cell to the goal. 
#
# If a cell is a wall or it is impossible to reach the goal from a cell,
# assign that cell a value of 99.
# ----------

grid = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1 # the cost associated with moving from a cell to an adjacent one

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>']

def compute_value(grid,goal,cost):
    # ----------------------------------------
    # insert code below
    # ----------------------------------------
    value = [[99 for col in range(len(grid[0]))] for row in range(len(grid))]
    value[goal[0]][goal[1]] = 0
    flags = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]
    open = [[0] + goal]
    while len(open) > 0:
        open.sort() #sort by g value
        open.reverse()
        next = open.pop()
        x = next[1]
        y = next[2]
        g = next[0]
        for motion in delta:
            x1 = x + motion[0]
            y1 = y + motion[1]
            g1 = g + cost
            if x1 >= 0 and x1 < len(grid) and y1 >= 0  and y1 < len(grid[0]):
                #if x1 and y2 are within range
                if grid[x1][y1] == 0 and flags[x1][y1] == 0:
                    #if x1 and y2 are not walls and have not been closed
                    open.append([g1, x1, y1])
                    value[x1][y1] = g1
        flags[x][y] = 1 #close this element 
                    
    
    # make sure your function returns a grid of values as 
    # demonstrated in the previous video.
    return value 
a = compute_value(grid,goal,cost)
for row in a:
    print(row)
