class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, w):
        self.edges.append((u, v, w))

def kruskal(graph):
    graph.edges = sorted(graph.edges, key=lambda x: x[2])
    parent = [i for i in range(graph.vertices)]
    result = []
    index = 0

    while len(result) < graph.vertices - 1:
        u, v, w = graph.edges[index]
        index += 1
        x = find(parent, u)
        y = find(parent, v)

        if x != y:
            result.append((u, v, w))
            union(parent, x, y)

    return result

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, x, y):
    x_set = find(parent, x)
    y_set = find(parent, y)
    parent[x_set] = y_set

# Take user input for the graph
vertices = int(input("Enter the number of vertices: "))
edges = int(input("Enter the number of edges: "))
graph = Graph(vertices)

print("Enter the edges (u v w) where u and v are vertices and w is the weight:")
for _ in range(edges):
    u, v, w = map(int, input().split())
    graph.add_edge(u - 1, v - 1, w)

# Find the minimum spanning tree
result = kruskal(graph)

# Print the result
print("\nMinimum Spanning Tree:")
for u, v, w in result:
    print(f"{u + 1} - {v + 1} : {w}")
