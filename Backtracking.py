#%%
def count_maze_solutions(maze, position = (0, 0)):
    row, col = position
    N, M = len(maze) - 1, len(maze[0]) - 1
    count = 0
    if position == (N, M):
        return 1
    if row < N and maze[row+1][col]:
        count += count_maze_solutions(maze, (row + 1,col))
    if col < M and maze[row][col + 1]:
        count += count_maze_solutions(maze, (row, col + 1))
    return count