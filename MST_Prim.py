class Device:
    def __init__(self, id, parentId, wireLength):
        self.id = id
        self.parentId = parentId
        self.wireLength = wireLength
        self.children = []

def calculateTotalWireLength(device):
    global totalWireLength
    for child in device.children:
        totalWireLength += child.wireLength
        calculateTotalWireLength(child)

def prim_minimum_spanning_tree(devices):
    n = len(devices)
    min_spanning_tree = []

    # Set to keep track of vertices included in the minimum spanning tree
    included = set([devices[0]])

    while len(included) < n:
        min_edge = None

        # Iterate over all included vertices
        for node in included:
            # Iterate over all adjacent vertices of the included vertex
            for child in node.children:
                if child not in included and (min_edge is None or child.wireLength < min_edge.wireLength):
                    min_edge = child

        if min_edge:
            min_spanning_tree.append((min_edge.parentId, min_edge.id, min_edge.wireLength))
            included.add(min_edge)

    return min_spanning_tree

if __name__ == "__main__":
    totalWireLength = 0
    n = int(input("Enter the number of devices (N): "))
 
    devices = [Device(i + 1, -1, 0) for i in range(n)]
    
    for i in range(n - 1):
        print(f"Enter device connection (D{i + 1} D{i + 2} L): ", end="")
        device1, device2, wireLength = map(int, input().split())
        parent = devices[device1 - 1]
        child = devices[device2 - 1]
        child.parentId = device1
        child.wireLength = wireLength
        parent.children.append(child)
    
    totalWireLength = 0
    calculateTotalWireLength(devices[0])
    print("Minimum length of wire to connect all devices:", totalWireLength)

    # Find and print the minimum spanning tree using Prim's algorithm
    min_spanning_tree = prim_minimum_spanning_tree(devices)
    print("Minimum Spanning Tree:")
    for edge in min_spanning_tree:
        print(f"Device {edge[0]} - Device {edge[1]}: {edge[2]}")


#Enter the number of devices (N): 5
#Enter device connection (D1 D2 L): 1 2 10
#Enter device connection (D2 D3 L): 2 3 15
#Enter device connection (D3 D4 L): 3 4 20
#Enter device connection (D4 D5 L): 4 5 25
