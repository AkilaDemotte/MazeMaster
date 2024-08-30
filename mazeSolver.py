# library to create a Maze
from pyamaze import maze, agent, COLOR

# DFS algorithm to solve the maze


def DFS(m):
    # Start position is the bottom right corner of the maze
    start = (m.rows, m.cols)
    # explored is a list of cells that have been visited
    explored = [start]
    # frontier is a list of cells that are yet to be visited
    frontier = [start]
    # dfsPath is a dictionary that stores the path from the start to the current cell in the reverse order
    dfsPath = {}
    # while the frontier is not empty, pop the last element from the frontier and check if it is the start cell
    while len(frontier) > 0:
        currCell = frontier.pop()
        if currCell == (1, 1):
            break
        # for each direction, check if the cell is a valid cell and if it has been visited
        for i in 'ESNW':
            # m.maze_map is a 2D list that stores the maze
            # if traversing in the direction i is possible, then the next cell is calculated
            if m.maze_map[currCell][i] == True:
                if i == 'E':
                    nextCell = (currCell[0], currCell[1]+1)
                elif i == 'S':
                    nextCell = (currCell[0]+1, currCell[1])
                elif i == 'N':
                    nextCell = (currCell[0]-1, currCell[1])
                elif i == 'W':
                    nextCell = (currCell[0], currCell[1]-1)
                    # if the next cell has already been visited, then continue to the next cell
                if nextCell in explored:
                    continue
                # if the next cell has not been visited, then add it to the explored list and the frontier list
                explored.append(nextCell)
                frontier.append(nextCell)
                # add the path from the current cell to the next cell in the dfsPath dictionary
                dfsPath[nextCell] = currCell
    # since the path is stored in the reverse order, we need to reverse it to get the path from the start to the end
    fwdPath = {}
    cell = (1, 1)
    while cell != start:
        fwdPath[dfsPath[cell]] = cell
        cell = dfsPath[cell]
    return fwdPath


# Create a maze of size 10x10
m = maze(20, 20)
m.CreateMaze()
# Get the path from the start to the end of the maze
path = DFS(m)
# Create an agent that will traverse the maze
a = agent(m, footprints=True, shape='arrow')
# Trace the path from the start to the end of the maze
m.tracePath({a: path})
print(m.maze_map)
# Run the maze
m.run()
