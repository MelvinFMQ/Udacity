# ----------
# User Instructions:
# 
# Implement the function optimum_policy2D below.
#
# You are given a car in grid with initial state
# init. Your task is to compute and return the car's 
# optimal path to the position specified in goal; 
# the costs for each motion are as defined in cost.
#
# There are four motion directions: up, left, down, and right.
# Increasing the index in this array corresponds to making a
# a left turn, and decreasing the index corresponds to making a 
# right turn.

grid = [[0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0]]
init = [0, 0, 3]
goal = [4, 2]
cost = [10, 40, 65]


forward = [[-1,  0], # go up
           [ 0, -1], # go left
           [ 1,  0], # go down
           [ 0,  1]] # go right
forward_name = ['up', 'left', 'down', 'right']

# action has 3 values: right turn, no turn, left turn
action = [-1, 0, 1]
action_name = ['R', '#', 'L']

# EXAMPLE INPUTS:
# grid format:
#     0 = navigable space
#     1 = unnavigable space 
grid_old = [[1, 1, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1]]

init_old = [4, 3, 0] # given in the form [row,col,direction]
                 # direction = 0: up
                 #             1: left
                 #             2: down
                 #             3: right
                
goal_old = [2, 0] # given in the form [row,col]

cost_old = [2, 1, 1] # cost has 3 values, corresponding to making 
                  # a right turn, no turn, and a left turn

# EXAMPLE OUTPUT:
# calling optimum_policy2D with the given parameters should return 
# [[' ', ' ', ' ', 'R', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', '#'],
#  ['*', '#', '#', '#', '#', 'R'],
#  [' ', ' ', ' ', '#', ' ', ' '],
#  [' ', ' ', ' ', '#', ' ', ' ']]
# ----------

# ----------------------------------------
# modify code below
# ----------------------------------------
class path:
    def __init__(self, x, y, o):
        self.x = x
        self.y = y
        self.o = 0
        self.right  = None
        self.straight = None
        self.left = None
    def add(self, action, x ,y , o):
        if action == 0:
            self.right = path(x,y,o)
            return self.right
        elif action == 1:
            self.straight = path(x,y,o)
            return self.straight
        else:
            self.left = path(x,y,o)
            return self.left
    def traverse(self, goal, policy2D):
        print(self.x , self.y)
        print(policy2D)

        if self.x == goal[0] and self.y == goal[1]:
            print('hi')
            return True #return this node reached the end
        if self.straight is not None:
            result = self.straight.traverse(goal, policy2D)
            print(self.x, self.y, result)
            if result:
                print('hi')
                policy2D[self.x][self.y] = '#'
                return True
        if self.right is not None:
            result = self.right.traverse(goal, policy2D)
            if result:
                policy2D[self.x][self.y] = 'R'
                return True

        if self.left is not None:
            result = self.left.traverse(goal, policy2D)
            if result:
                policy2D[self.x][self.y] = 'L'
                return True
        return False

        

def optimum_policy2D(grid,init,goal,cost):
    start = path(init[0], init[1], init[2])
    open = [[0] + init + [start]]
    policy2D = [[' ' for cols in range(len(grid[0]))] for row in range(len(grid))]
    policy2D[goal[0]][goal[1]] = '*'
    min_dis = len(grid) * len(grid[0]) * max(cost)
    while len(open) > 0:
        print(open)
        open.sort()
        open.reverse()
        next = open.pop()
        x = next[1]
        y = next[2]
        g = next[0]
        o = next[3] #orientation
        p = next[4]
        for a in range(len(action)): #a for action
            turn = action[a]
            #-1 for right, 0 for straight, 1 for left --> turns 
            #0 for up, 1 for left , 2 for down, 3 for right --> orientaion 
            o1 = (o + turn) % 4 #turn to correct orientation 
            x1 = x + forward[o1][0]
            y1 = y + forward[o1][1]
            cost1 = cost[a]
            g1 = g + cost1
            if x1 >= 0 and x1 < len(grid) and y1 >= 0 and y1 < len(grid[0]):
                #if new x and y are within ranges
                if grid[x1][y1] == 0:
                    #if x1 and y1 are not walls
                    if x1 == goal[0] and y1 == goal[1]:
                        #hit the goal
                        if g1 < min_dis:
                            min_dis = g1
                            p.add(a, x1, y1, o1)
                    if g1 < min_dis:
                        print('x', x1, 'y', y1)
                        tmp_p = p.add(a, x1, y1, o1)
                        open.append([g1, x1, y1, o1, tmp_p])
                    #print('orientation', o1, 'turn', turn, 'a', a, action_name[a], cost1)
    print(policy2D)
    start.traverse(goal, policy2D)        
    return policy2D
a = optimum_policy2D(grid,init,goal,cost)
for row in a:
    print(row)
