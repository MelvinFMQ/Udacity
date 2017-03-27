# --------------
# USER INSTRUCTIONS
#
# Write a function called stochastic_value that 
# returns two grids. The first grid, value, should 
# contain the computed value of each cell as shown 
# in the video. The second grid, policy, should 
# contain the optimum policy for each cell.
#
# --------------
# GRADING NOTES
#
# We will be calling your stochastic_value function
# with several different grids and different values
# of success_prob, collision_cost, and cost_step.
# In order to be marked correct, your function must
# RETURN (it does not have to print) two grids,
# value and policy.
#
# When grading your value grid, we will compare the
# value of each cell with the true value according
# to this model. If your answer for each cell
# is sufficiently close to the correct answer
# (within 0.001), you will be marked as correct.

delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

# ---------------------------------------------
#  Modify the function stochastic_value below
# ---------------------------------------------

def stochastic_value(grid,goal,cost_step,collision_cost,success_prob):
    failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
    value = [[collision_cost for col in range(len(grid[0]))] for row in range(len(grid))]
    policy = [[' ' for col in range(len(grid[0]))] for row in range(len(grid))]
    changed = True
    value[goal[0]][goal[1]] = 0
    while changed:
        changed = False
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                for a in range(len(delta)):
                    if grid[x][y] != 1: #cannot come from wall
                        x1 = x + delta[a][0]
                        y1 = y + delta[a][1]
                        if x1 >= 0 and x1 < len(grid) and y1 >= 0 and y1 < len(grid[0]) and grid[x1][y1] != 1:
                            #within range and not a wall
                            forward = success_prob * value[x1][y1]
                        else:
                            forward = success_prob * collision_cost
                        left = (a + 1) % 4
                        right = (a + 3) % 4
                        #print('dir', delta_name[a])
                        #print('left', delta_name[left])
                        #print('right', delta_name[right])
                        x2 = x + delta[left][0]
                        y2 = y + delta[left][1]
                        x3 = x + delta[right][0]
                        y3 = y + delta[right][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] != 1:
                            #within range and not a wall
                            right = value[x2][y2] * failure_prob
                        else:
                            #if outside or wall
                            right = collision_cost * failure_prob 
                        if x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[0]) and grid[x3][y3] != 1:
                            #within range and not a wall
                            left = value[x3][y3] * failure_prob
                        else:
                            #if outside or wall
                            left = collision_cost * failure_prob                            
                        g1 = forward + left + right + cost_step
                        #print('left', left, 'right', right, 'forward', forward)
                        #print('x', x, 'y', y)
                        if g1 < value[x][y]:
                            value[x][y] = g1
                            policy[x][y] = delta_name[a]
                            changed = True
                            #print('left', left, 'right', right, 'forward', forward)
                            #print('x', x, 'y', y)
                            
                    
                    
    return value, policy

# ---------------------------------------------
#  Use the code below to test your solution
# ---------------------------------------------

grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
goal = [0, len(grid[0])-1] # Goal is in top right corner
cost_step = 1
collision_cost = 100
success_prob = 0.5

value,policy = stochastic_value(grid,goal,cost_step,collision_cost,success_prob)
for row in value:
    print(row)
for row in policy:
    print(row)

# Expected outputs:
#
# [57.9029, 40.2784, 26.0665,  0.0000]
# [47.0547, 36.5722, 29.9937, 27.2698]
# [53.1715, 42.0228, 37.7755, 45.0916]
# [77.5858, 100.00, 100.00, 73.5458]
#
# ['>', 'v', 'v', '*']
# ['>', '>', '^', '<']
# ['>', '^', '^', '<']
# ['^', ' ', ' ', '^']
