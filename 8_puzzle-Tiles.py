import math
from queue import PriorityQueue
import random
import copy

target = ((1, 2, 3),
          (4, 5, 6),
          (7, 8, 0))


def ZeroSearch(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] == 0:
                return i, j


def get_children(grid):
    nextPStates=[]
    tempStates=[]
    children = []
    bx, by = ZeroSearch(grid)
    if bx < 2:
        temp = [list(i) for i in grid]
        temp[bx][by], temp[bx + 1][by] = temp[bx + 1][by], temp[bx][by]
        t = tuple(tuple(i) for i in temp)
        children.append(t)
    if bx > 0:
        temp = [list(i) for i in grid]
        temp[bx][by], temp[bx - 1][by] = temp[bx - 1][by], temp[bx][by]
        t = tuple(tuple(i) for i in temp)
        children.append(t)

    if by < 2:
        temp = [list(i) for i in grid]
        temp[bx][by], temp[bx][by + 1] = temp[bx][by + 1], temp[bx][by]
        t = tuple(tuple(i) for i in temp)
        children.append(t)

    if by > 0:
        temp = [list(i) for i in grid]
        temp[bx][by], temp[bx][by - 1] = temp[bx][by - 1], temp[bx][by]
        t = tuple(tuple(i) for i in temp)
        children.append(t)

    return children


def HuetCost(pathState, chooseHeut):
    if chooseHeut == 1:
        return 0

    if chooseHeut == 2:
        cost = 0
        for i in range(3):
            for j in range(3):
                if pathState[i][j] == 0 or pathState[i][j] == target[i][j]:
                    continue
                else:
                    cost += 1
        return cost

    if chooseHeut == 3: 
        cost = 0
        for i in range(3):
            for j in range(3):
                if pathState[i][j] == 0:
                    continue
                x = int((pathState[i][j] - 1) / 3)
                y = (pathState[i][j] - 1) % 3
                cost += (abs(x - i) + abs(y - j))
        return cost

    if chooseHeut == 4:  
        cost = 0
        for i in range(3):
            for j in range(3):
                if pathState[i][j] == 0:
                    continue
                x = int((pathState[i][j] - 1) / 3)
                y = (pathState[i][j] - 1) % 3
                cost += x**3+y**3
                # math.sqrt((x - i) ** 2 + (y - j) ** 2)
        return cost


def AnsShow(grid, h_i):
    print()
    if h_i == 1:
        print("Now when heuristic cost is 0")

    elif h_i == 2:
        print("When heuristic cost is equal to Number of tiles displaced")

    elif h_i == 3:
        print("Now taking Manhattan distance as heuristic Cost")

    elif h_i == 4:
        print("Now Taking Random Function")

    CordX, CordY = ZeroSearch(grid)
    open_list = PriorityQueue()
    open_list.put([HuetCost(grid, h_i), grid])
    dist = {grid: 0}
    closed_list = set()
    while open_list:
        prior, curr_state = open_list.get()
        if curr_state == target:
            print("Target State reached.")
            print("Total states in optimal path ", dist[target] + 1)
            print("Total number of states explored is ", len(closed_list))
            return

        CordX, CordY = ZeroSearch(curr_state)
        children = get_children(curr_state)
        for i in children:
            i = tuple(tuple(j) for j in i)
            if i not in closed_list and (i not in dist or dist[i] > dist[curr_state] + 1):
                dist[i] = dist[curr_state] + 1
                open_list.put([HuetCost(i, h_i) + dist[i], i])

            closed_list.add(curr_state)

    print("Target State not found.")
    print("Number of States visited is ", len(closed_list))
    return


temp_grid = [1,2,3,0,4,6,7,5,8]
# random.shuffle(temp_grid)

initGraph = ((temp_grid[0], temp_grid[1], temp_grid[2]),
                (temp_grid[3], temp_grid[4], temp_grid[5]),
                (temp_grid[6], temp_grid[7], temp_grid[8]))



print("Initial grid is: ")
print(initGraph)
alpha=int(input().strip())
AnsShow(initGraph,alpha)
