#Q.2 Write a Python program to implement the Depth First Search (DFS) algorithm. Refer to the following graph as input for
 #the program. [Initial node = 1, Goal node = 8].
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

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  

    if start == goal:
        return True  

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

print("DFS traversal path:")
dfs(graph, 1, 8)


#Output:
#DFS traversal path:
#1 2 4 8