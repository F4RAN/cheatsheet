def dfs(matrix, i, j):
    # Boundary checks and check if the cell is water or already visited
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return

    # Mark the current cell as visited (turn it into water)
    matrix[i][j] = 0

    # Visit all adjacent cells (up, down, left, right)
    dfs(matrix, i + 1, j)  # Down
    dfs(matrix, i - 1, j)  # Up
    dfs(matrix, i, j + 1)  # Right
    dfs(matrix, i, j - 1)  # Left


def count_islands(matrix):
    if not matrix:
        return 0

    island_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:  # Start DFS if we find a land cell
                dfs(matrix, i, j)
                island_count += 1  # Increment island count

    return island_count


# Example usage
matrix = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1]
]
result = count_islands(matrix)
print(f"Number of islands: {result}")