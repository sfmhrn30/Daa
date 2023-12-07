class Device:
    def __init__(self, id, parentId, wireLength):
        self.id = id
        self.parentId = parentId
        self.wireLength = wireLength
        self.children = []

def findMinimumWireLengths(devices, deviceIndex):
    n = len(devices)
    distance = [float('inf')] * (n + 1)
    previous = [-1] * (n + 1)
    
    distance[deviceIndex] = 0

    # Bellman-Ford algorithm
    for _ in range(n - 1):
        for j in range(1, n + 1):
            for device in devices[j - 1].children:
                newDistance = distance[j] + device.wireLength
                if newDistance < distance[device.id]:
                    distance[device.id] = newDistance
                    previous[device.id] = j

    # Check for negative cycles
    for j in range(1, n + 1):
        for device in devices[j - 1].children:
            if distance[j] + device.wireLength < distance[device.id]:
                raise ValueError("Graph contains a negative cycle")

    return distance

if __name__ == "__main__":
    devices = []
    n = int(input("Enter the number of devices (N): "))

    for i in range(n):
        devices.append(Device(i + 1, -1, 0))

    for i in range(n - 1):
        print(f"Enter device connection (D{i + 1} D{i + 2} L): ", end="")
        device1, device2, wireLength = map(int, input().split())
        
        parent = devices[device1 - 1]
        child = devices[device2 - 1]
        child.parentId = device1
        child.wireLength = wireLength
        parent.children.append(child)

    print("Enter the device index (Di): ", end="")
    deviceIndex = int(input())

    minimumWireLengths = findMinimumWireLengths(devices, deviceIndex)
    
    print(f"Minimum length of wire to connect D{deviceIndex} to all other devices:")
    for i in range(1, len(minimumWireLengths)):
        print(f"To D{i}: {minimumWireLengths[i]}")
