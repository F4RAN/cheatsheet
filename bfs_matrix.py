from collections import deque


def bfs(matrix, i, j):
    queue = deque([(i, j)])
    matrix[i][j] = 0  # Mark the current cell as visited

    while queue:
        x, y = queue.popleft()

        # Check all 4 directions (up, down, left, right)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0  # Mark visited


def count_islands(matrix):
    if not matrix:
        return 0

    island_count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:  # Start BFS if we find a land cell
                bfs(matrix, i, j)
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
