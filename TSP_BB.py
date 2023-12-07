import numpy as np

class TSPBranchBound:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.visited = [False] * self.n
        self.min_cost = float('inf')
        self.best_path = []

    def solve(self):
        start_vertex = int(input("Enter the starting vertex (0 to {}): ".format(self.n - 1)))
        self.visited[start_vertex] = True
        self.branch_and_bound(start_vertex, [start_vertex], 0)

    def branch_and_bound(self, current_vertex, path, cost):
        if len(path) == self.n:
            if self.graph[current_vertex][path[0]] + cost < self.min_cost:
                self.min_cost = self.graph[current_vertex][path[0]] + cost
                self.best_path = path + [path[0]]
            return

        for next_vertex in range(self.n):
            if not self.visited[next_vertex]:
                if cost + self.graph[current_vertex][next_vertex] < self.min_cost:
                    self.visited[next_vertex] = True
                    self.branch_and_bound(next_vertex, path + [next_vertex],
                                           cost + self.graph[current_vertex][next_vertex])
                    self.visited[next_vertex] = False

    def get_min_cost(self):
        return self.min_cost

    def get_best_path(self):
        return self.best_path

# Take user inputs for the graph
n = int(input("Enter the number of vertices in the graph: "))
graph = np.zeros((n, n), dtype=int)
print("Enter the adjacency matrix:")
for i in range(n):
    graph[i] = list(map(int, input().split()))

tsp_solver = TSPBranchBound(graph)
tsp_solver.solve()
min_cost = tsp_solver.get_min_cost()
best_path = tsp_solver.get_best_path()
print("Minimum Cost:", min_cost)
print("Best Path:", best_path)
