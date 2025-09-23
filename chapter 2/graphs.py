"""Data Structure : Graphs"""

""" A graph consists of a set of vertices (or nodes)"""
""" A set of edges that connect pairs of vertices."""

""" Creating a graph """

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

"""Creating a graph"""
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')


A.neighbors = [B, C, D]
B.neighbors = [A, E]
C.neighbors = [A, F]
D.neighbors = [A, G, H]
E.neighbors = [B]
F.neighbors = [C]
G.neighbors = [D, H]
H.neighbors = [D, G]



""" Traversing a graph """

"""Common ways to traverse in graph"""
"""Depth-first Search"""

def dfs(node, visited):
    visited.add(node)
    print(node.data)
    for neighbor in node.neighbors:
        if neighbor not in visited:
            dfs(neighbor, visited)

# DFS traversal of the graph
visited = set()
dfs(A, visited)


"""Breadth-first search(BFS)"""

def bfs(node):
    visited = set()
    queue = [node]
    visited.add(node)
    while queue:
        curr_node = queue.pop(0)
        print(curr_node.data)
        for neighbor in node.neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
        

# BFS traversal of the graph
bfs(A)

"""Finding paths in a graph"""
"""We can use either DFS or BFS to perform traversal"""

def find_path(start_node, end_node, visited, path):
    visited.add(start_node)
    path.append(start_node)
    if start_node == end_node:
        return path
    
    for neighbor in start_node.neighbors:
        if neighbor not in visited:
            result = find_path(neighbor, end_node, visited, path)
            if result:
                return result
        path.pop()

    # Finding a graph in the graph
    visited = set()
    path = []
    result = find_path(A, H, visited, path)
    if result:
        print("Path found:", [node.data for node in result])
    else:
        print("Path not found")