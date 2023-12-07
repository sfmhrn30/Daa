#Di 1<=i<=N
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
    for i in range(1, num_devices):
        for device in graph.devices:
            u = device.id
            for child in device.children:
                v = child.id
                weight = child.wireLength
                if graph.dist[u] != float('inf') and graph.dist[u] + weight < graph.dist[v]:
                    graph.dist[v] = graph.dist[u] + weight

if __name__ == "__main__":
    print("Enter the number of devices (N): ")
    n = int(input())
    devices = [Device(i + 1, -1, 0) for i in range(n)]

    for i in range(n - 1):
        print(f"Enter device connection (D{i + 1} D{i + 2} L): ")
        device1, device2, wireLength = map(int, input().split())
        devices[device1 - 1].children.append(devices[device2 - 1])
        devices[device2 - 1].parentId = device1
        devices[device2 - 1].wireLength = wireLength

    print("Enter the device index (Di): ")
    deviceIndex = int(input())
    graph = Graph(devices)
    num_devices = len(devices)
    graph.dist = [float('inf')] * (num_devices + 1)
    graph.dist[deviceIndex] = 0
    bellman_ford(graph, deviceIndex)

    print("Minimum length of wire to connect D{} to all other devices:".format(deviceIndex))
    for i in range(1, num_devices + 1):
        if i != deviceIndex:
            print("To D{}: {}".format(i, graph.dist[i]))


#Enter the number of devices (N): 
#3
#Enter device connection (D1 D2 L): 
#1 2 3
#Enter device connection (D2 D3 L): 
#2 3 2
#Enter the device index (Di): 
#1
#Minimum length of wire to connect D1 to all other devices:
#To D2: 3
#To D3: 5