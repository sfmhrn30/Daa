INF = float('inf')

def floyd_warshall(graph):
    n = len(graph)
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# Take user input for the graph
n = int(input("Enter the number of vertices: "))
graph = []

print("Enter the adjacency matrix for the graph (Enter INF for infinity):")
for i in range(n):
    row = []
    for j in range(n):
        weight = float('inf') if i == j else float(input(f"Enter weight from vertex {i+1} to {j+1}: "))
        row.append(weight)
    graph.append(row)

# Perform Floyd-Warshall algorithm
result = floyd_warshall(graph)

# Print the result
print("\nAll-Pairs Shortest Paths (Floyd-Warshall Algorithm):")
for row in result:
    print(row)
