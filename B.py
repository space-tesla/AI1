#Q.2 Write a Python program to implement the Depth First Search (DFS) algorithm. Refer to the following graph as input for
 #the program. [Initial node = 1, Goal node = 8].
  1
 / \
2   3
|\  |\
4 5 6 7
 \|/|/
  8
# Define the graph as an adjacency list
graph = {
    1: [2, 3],
    2: [4, 5],
    3: [6, 7],
    4: [8],
    5: [8],
    6: [8],
    7: [8],
    8: []
}

# Depth First Search function
def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  # Print the current node

    if start == goal:
        return True  # Goal node found

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

# Initialize DFS from node 1 to find node 8
print("DFS traversal path:")
dfs(graph, 1, 8)

#Output:
#DFS traversal path:
#1 2 4 8