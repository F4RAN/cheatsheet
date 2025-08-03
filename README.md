# cheatsheet
Python Cheatsheet: [Here](https://github.com/F4RAN/cheatsheet/blob/main/PY.md)

## Algorithms:
[1- Binary Search](https://github.com/F4RAN/cheatsheet/blob/main/binary_search.py)

[2- Breadth-First Search](https://github.com/F4RAN/cheatsheet/blob/main/bfs.py)
- [2.1- BFS in Matrix](https://github.com/F4RAN/cheatsheet/blob/main/bfs_matrix.py)

[3- Depth-First Search (Backtrack)](https://github.com/F4RAN/cheatsheet/blob/main/dfs.py)
- [3.1- DFS in Matrix](https://github.com/F4RAN/cheatsheet/blob/main/dfs_matrix.py)
- [3.2- DFS in RegEx Match](https://github.com/F4RAN/cheatsheet/blob/main/dfs_regex_match.py) ([Video tutorial](https://www.youtube.com/watch?v=HAA8mgxlov8&t=240s))

[4- Sliding Window](https://github.com/F4RAN/cheatsheet/blob/main/sliding_window.py)

[5- Two Pointers](https://github.com/F4RAN/cheatsheet/blob/main/two_pointers_max_area.py) ([11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/description/))
- [5.1- Swap Nodes in Pairs (Linked list)](https://github.com/F4RAN/cheatsheet/blob/main/two_pointers_swap_linked_list.py) ([24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/description/))

[6- Math]()
- [6.1- Division using shift](https://github.com/F4RAN/cheatsheet/blob/main/math_divide.py) ([29. Divide Two Integers](https://leetcode.com/problems/divide-two-integers))

[7- Graphs]()
- [7.1- Floyd's Law (Has written bottom: Graphs - 1) ([141. Linked List Cycle](https://leetcode.com/problems/divide-two-integers](https://leetcode.com/problems/linked-list-cycle/)))
- 
## Applications:

### Graphs
1) ** The Cycle Meeting Law (Floyd’s Principle) **
In a closed loop (cycle) of length k, if two agents move in the same direction at constant speeds and the faster agent moves r steps more than the slower agent per turn (where r > 0), the faster agent will always meet the slower agent in at most k / gcd(k, r) turns.



### BFS

1) **Shortest Path in an Unweighted Graph:**
BFS is used to find the shortest path between two nodes in an unweighted graph (or grid) since it explores all nodes at the present "depth" level before moving on to the next.

2) **Level-Order Traversal in Trees:**
BFS is used to traverse a tree level by level, which is also known as level-order traversal.

3) **Connected Components in Graphs**:
BFS helps in finding all connected components in a graph. It explores all nodes connected to a starting node.

4) **Cycle Detection in Undirected Graphs:**
BFS can be used to detect cycles in an undirected graph by checking if a node is visited twice.

5) **Finding the Minimum Number of Moves (Grid Problems):**
BFS is commonly used in grid-based puzzles (like finding the shortest path in a maze) to determine the minimum number of moves required to reach a target.

6) **Peer-to-Peer Networks:**
BFS is used to broadcast messages in peer-to-peer networks, ensuring that all nodes are reached in the minimum number of hops.

7) **Crawlers in Search Engines:**
BFS is employed by web crawlers to explore and index web pages level by level, starting from a seed URL.

8) **Social Networking Sites**:
BFS is used to determine the shortest path or degrees of separation between users.

9) **Finding All Nodes at a Distance K**:
BFS is useful for finding all nodes that are at a distance K from a given node in a graph.

### DFS
1) **Pathfinding and Maze Solving:**
DFS is used to explore all possible paths in a maze or a puzzle, particularly in backtracking problems.

2) **Connected Components in Graphs**:
Like BFS, DFS can also be used to find connected components in a graph.

3) **Cycle Detection in Directed Graphs:**
DFS is useful in detecting cycles in directed graphs by checking back edges during traversal.

4) **Topological Sorting:**
DFS is used in topological sorting of a directed acyclic graph (DAG). This is useful in scheduling problems where certain tasks must be completed before others.

5) **Finding Strongly Connected Components:**
Tarjan’s or Kosaraju’s algorithm, based on DFS, is used to find all strongly connected components in a directed graph.

6) **Artificial Intelligence (AI) for Game Playing:**
DFS is applied in game tree exploration, such as in depth-limited search and iterative deepening search.

7) **Solving Puzzles:**
DFS is applied in solving puzzles like Sudoku, N-Queens, and crosswords, where all possible configurations need to be checked.

8) **Decision Trees:**
DFS is used in constructing and exploring decision trees, often used in machine learning.

9) **Generating Permutations and Combinations:**
DFS can be used to generate all permutations or combinations of a set of items.

10) **Finding Bridges and Articulation Points:**
DFS can identify critical edges and vertices in a graph whose removal would increase the number of connected components. 

### Binary Search
1) **Finding an Element in a Sorted Array:**
The most common application of binary search is to quickly find an element in a sorted array.

2) **Finding the Lower and Upper Bounds:**
Binary search is used to find the first or last occurrence of a given value in a sorted array, which is helpful in range queries.

3) **Search in a Rotated Sorted Array:**
Binary search can be modified to find an element in a rotated sorted array efficiently.

4) **Finding the Square Root (or Nth Root):**
Binary search can approximate the square root (or any Nth root) of a number to a specified precision.

5) **Searching in Infinite or Very Large Arrays:**
Binary search can be used to search efficiently in infinite or very large sorted arrays where the size is not known upfront.

6) **Finding the Peak Element:**
Binary search can be used to find a peak element in an array where the array is not necessarily sorted.

7) **Minimum in Rotated Sorted Array:**
Binary search is used to find the minimum element in a rotated sorted array.

8) **Kth Smallest/Largest Element:**
Binary search can be applied in selection algorithms to find the Kth smallest or largest element in sorted or partially sorted structures.

9) **Optimize Monotonic Functions:**
Binary search is used in optimization problems where the function is monotonic, such as finding the point where a function changes behavior.

10) **Dictionary Lookup:**
Binary search is used in dictionary data structures where keys are stored in sorted order to quickly find a value.

### Sliding Window
1) **Finding Maximum or Minimum Sum of a Subarray:**
Sliding window is commonly used to find the maximum or minimum sum of k consecutive elements in an array.

2) **Longest Substring Without Repeating Characters:**
Sliding window helps in finding the length of the longest substring without repeating characters in a string.

3) **Smallest Subarray with a Given Sum:**
It’s used to find the length of the smallest contiguous subarray whose sum is greater than or equal to a given number.

4) **Maximum of All Subarrays of Size K:**
Sliding window can be used to find the maximum element in all subarrays of size k.

5) **Substring Anagrams:**
Sliding window is used to find all starting indices of substring(s) in a string that is an anagram of a given pattern.

6) **Fixed-Window Mean/Median Calculation:**
Sliding window is used in real-time data processing to maintain and update the mean or median of the last k elements.

7) **Dynamic Window Problems:**
Problems that involve dynamically adjusting the size of the window based on certain conditions, like the longest substring with at most k distinct characters.

8) **Two Pointer Techniques:**
Sliding window is often combined with two-pointer techniques to solve problems like finding pairs in an array that satisfy a given condition.

9) **Finding Substrings with Exactly K Distinct Characters:**
Sliding window can be used to find all substrings that contain exactly k distinct characters.

10) **Image Processing:**
Sliding window techniques are applied in computer vision tasks, like object detection, where the window slides over the image to detect objects of interest.
