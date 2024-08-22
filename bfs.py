"""
We should visit all nodes which connected to the one node (neighbours) then go to the next node
https://www.youtube.com/watch?v=PMMc4VsIacU
   A
  / \
 B   C
 |   |
 D   F
 |   |
 E---|

"""
from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")  # Process the node (here we just print it)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['D', 'F'],
    'F': ['C', 'E']
}
bfs(graph, 'A')
