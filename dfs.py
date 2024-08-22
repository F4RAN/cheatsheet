"""
   A
  / \
 B   C
 |   |
 D   F
 |   |
 E---|
"""
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start, end=" ")  # Process the node (here we just print it)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'F'],
    'D': ['B', 'E'],
    'E': ['D', 'F'],
    'F': ['C', 'E']
}
dfs(graph, 'A')
