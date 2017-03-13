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

def search(grid,init,goal,cost):
    # ----------------------------------------
    # insert code here
    # ----------------------------------------
    open_a = [[0, init[0], init[1]]]
    flags = [False]
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    while False in flags:
        min_g_index = 0
        while flags[min_g_index] == True:
            min_g_index += 1
        #expansion
        gvalue, x, y = open_a[min_g_index]
        for deltax, deltay in delta:
            deltax = deltax + x
            deltay = deltay + y
            if deltax > max_x or deltax < 0 or deltay > max_y or deltay < 0 or grid[deltax][deltay] == 1:
                #if x or y is to small or big or is a wall
                pass
                #print('x', deltax , 'y', deltay)
            else:
                found = False
                tmp = [gvalue + cost, deltax , deltay]
                for index in range(len(open_a)):
                    old_g_value, tmpx , tmpy = open_a[index]
                    if tmpx == deltax and tmpy == deltay:
                        if old_g_value > gvalue + 1: #old one is more than new one, replace
                            open_a[index] = tmp
                        found = True
                        print('Found', 'x', deltax , 'y', deltay)
                #else not found, append
                if not found: 
                    open_a.append(tmp)
                    flags.append(False)
                    print('Not found','x', deltax , 'y', deltay)
                #if its the goal, end.
                if [deltax,deltay] == goal:
                    return tmp
        flags[min_g_index] = True
    return 'fail'

print(search(grid,init,goal,cost))
