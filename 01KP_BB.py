class KnapsackNode:
    def __init__(self, level, value, weight, include):
        self.level = level
        self.value = value
        self.weight = weight
        self.include = include

def knapsack_branch_and_bound(weights, values, capacity):
    n = len(weights)
    value_per_weight = [(i, values[i] / weights[i]) for i in range(n)]
    value_per_weight.sort(key=lambda x: x[1], reverse=True)
    max_value = 0
    best_taken = None
    
    def bound(node):
        if node.weight > capacity:
            return 0
        bound_value = node.value
        bound_weight = node.weight
        j = node.level + 1
        while j < n and bound_weight + weights[value_per_weight[j][0]] <= capacity:
            bound_value += values[value_per_weight[j][0]]
            bound_weight += weights[value_per_weight[j][0]]
            j += 1
        if j < n:
            bound_value += (capacity - bound_weight) * value_per_weight[j][1]
        return bound_value

    def knapsack_recursive(node):
        nonlocal max_value, best_taken
        if node.level == n - 1:
            if node.value > max_value:
                max_value = node.value
                best_taken = node.include.copy()
        else:
            include_node = KnapsackNode(node.level + 1,
                                        node.value + values[value_per_weight[node.level + 1][0]],
                                        node.weight + weights[value_per_weight[node.level + 1][0]],
                                        node.include + [value_per_weight[node.level + 1][0]])
            exclude_node = KnapsackNode(node.level + 1, node.value, node.weight, node.include.copy())
            if bound(include_node) > max_value:
                knapsack_recursive(include_node)
            if bound(exclude_node) > max_value:
                knapsack_recursive(exclude_node)
    
    initial_node = KnapsackNode(-1, 0, 0, [])

    knapsack_recursive(initial_node)
    return max_value, best_taken

# Take user inputs
weights = list(map(int, input("Enter the weights of items separated by space: ").split()))
values = list(map(int, input("Enter the values of items separated by space: ").split()))
capacity = int(input("Enter the capacity of the knapsack: "))

# Call the function
max_value, best_taken = knapsack_branch_and_bound(weights, values, capacity)

# Display the result
print("Maximum Value:", max_value)
print("Items Taken:", best_taken)
