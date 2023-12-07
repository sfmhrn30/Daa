from queue import PriorityQueue

class Device:
    def __init__(self, id, parentId, wireLength):
        self.id = id
        self.parentId = parentId
        self.wireLength = wireLength
        self.children = []

class Graph:
    def __init__(self, devices):
        self.devices = devices

def bellman_ford(graph, source):
    num_devices = len(graph.devices)
    for i in range(num_devices):
        for device in graph.devices:
            u = device.id
            for child in device.children:
                v = child.id
                weight = child.wireLength
                if graph.dist[u] != float('inf') and graph.dist[u] + weight < graph.dist[v]:
                    graph.dist[v] = graph.dist[u] + weight

def dijkstra(graph, source):
    num_devices = len(graph.devices)
    visited = [False] * (num_devices + 1)
    distances = [float('inf')] * (num_devices + 1)
    distances[source] = 0
    queue = PriorityQueue()
    queue.put((0, source))

    while not queue.empty():
        dist_u, u = queue.get()
        visited[u] = True

        for device in graph.devices[u - 1].children:
            v = device.id
            weight = device.wireLength
            if not visited[v] and distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
                queue.put((distances[v], v))

    return distances[1:]

def johnson(graph):
    num_devices = len(graph.devices)

    # Add a new vertex with zero-weight edges to all other vertices
    new_vertex = Device(num_devices + 1, -1, 0)
    graph.devices.append(new_vertex)
    for device in graph.devices:
        if device != new_vertex:
            device.children.append(new_vertex)

    # Run Bellman-Ford on the modified graph
    graph.dist = [float('inf')] * (num_devices + 2)
    graph.dist[num_devices + 1] = 0
    bellman_ford(graph, num_devices + 1)

    # Update edge weights
    for device in graph.devices:
        for child in device.children:
            child.wireLength = child.wireLength + graph.dist[device.id] - graph.dist[child.id]

    # Remove the added vertex
    graph.devices.pop()

    # Run Dijkstra for each vertex to get the minimum distances
    all_pairs_distances = []
    for i in range(1, num_devices + 1):
        distances = dijkstra(graph, i)
        all_pairs_distances.append(distances)

    return all_pairs_distances

if __name__ == "__main__":
    n = int(input("Enter the number of devices (N): "))
    devices = [Device(i + 1, -1, 0) for i in range(n)]

    for i in range(n - 1):
        print(f"Enter device connection (D{i + 1} D{i + 2} L): ")
        device1, device2, wireLength = map(int, input().split())
        devices[device1 - 1].children.append(devices[device2 - 1])
        devices[device2 - 1].parentId = device1
        devices[device2 - 1].wireLength = wireLength

    graph = Graph(devices)

    # Run Johnson's algorithm
    all_pairs_distances = johnson(graph)

    # Print the results
    print("Shortest distances between all pairs of devices:")
    for i, distances in enumerate(all_pairs_distances, start=1):
        for j, distance in enumerate(distances, start=1):
            print(f"From D{i} to D{j}: {distance}")
