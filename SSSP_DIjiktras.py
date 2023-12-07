#single source Di to Dj.
from queue import PriorityQueue

class Device:
    def __init__(self, id, parentId, wireLength):
        self.id = id
        self.parentId = parentId
        self.wireLength = wireLength
        self.children = []

def find_minimum_wire_length(devices, device_index1, device_index2):
    n = len(devices)
    distance = [float('inf')] * (n + 1)
    previous = [-1] * (n + 1)

    distance[device_index1] = 0
    queue = PriorityQueue()
    queue.put(devices[device_index1 - 1])

    while not queue.empty():
        current = queue.get()
        if current.id == device_index2:
            return distance[current.id]

        for child in current.children:
            new_distance = distance[current.id] + child.wireLength
            if new_distance < distance[child.id]:
                distance[child.id] = new_distance
                previous[child.id] = current.id
                queue.put(child)

    return -1  # If no path exists

def main():
    n = int(input("Enter the number of devices (N): "))
    devices = [Device(i + 1, -1, 0) for i in range(n)]

    for i in range(n - 1):
        print(f"Enter device connection (D{i + 1} D{i + 2} L): ", end="")
        device1, device2, wire_length = map(int, input().split())

        parent = devices[device1 - 1]
        child = devices[device2 - 1]
        child.parentId = device1
        child.wireLength = wire_length
        parent.children.append(child)

    print("Enter device indices (Di Dj): ", end="")
    device_index1, device_index2 = map(int, input().split())

    minimum_wire_length = find_minimum_wire_length(devices, device_index1, device_index2)
    print(f"Minimum length of wire to connect D{device_index1} and D{device_index2}: {minimum_wire_length}")

if __name__ == "__main__":
    main()
